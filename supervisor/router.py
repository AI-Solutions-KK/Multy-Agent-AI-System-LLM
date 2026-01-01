# PATH: supervisor/router.py

from llm.client import GroqLLMClient
from agents.hr_agent import hr_agent
from agents.it_agent import it_agent
from sqlalchemy.orm import Session
from db.repositories import save_chat_message, get_last_messages

llm = GroqLLMClient()


def route_request(
    db: Session,
    message: str,
    session_id: str,
    user_id: str,
    user_role: str
) -> str:
    save_chat_message(db, session_id, "USER", f"[{user_role}] {message}")

    past = get_last_messages(db, session_id)
    context = "\n".join(f"{c.sender}: {c.message}" for c in reversed(past))

    prompt = f"""
You are a supervisor AI.

User role: {user_role}

Decide which agent should handle the request.
Return ONLY one word:
HR or IT

Conversation context:
{context}
"""

    decision = llm.generate(prompt).strip().upper()

    if "HR" in decision:
        response = hr_agent(db, message)
    elif "IT" in decision:
        response = it_agent(db, message)
    else:
        response = "Sorry, I could not understand the request."

    save_chat_message(db, session_id, "ASSISTANT", response)
    return response
