# PATH: agents/it_agent.py

from llm.client import GroqLLMClient
from tools.it_tools import create_it_ticket
from sqlalchemy.orm import Session
import uuid

llm = GroqLLMClient()


def it_agent(db: Session, message: str) -> str:
    prompt = f"""
Extract IT issue and priority.
Return STRICTLY in this format:
ISSUE=<issue>
PRIORITY=<priority>

Text:
{message}
"""

    response = llm.generate(prompt)

    issue = ""
    priority = "Medium"

    for line in response.splitlines():
        if line.startswith("ISSUE="):
            issue = line.replace("ISSUE=", "").strip()
        elif line.startswith("PRIORITY="):
            priority = line.replace("PRIORITY=", "").strip()

    if not issue:
        return "Failed to extract IT issue."

    ticket_id = f"IT-{uuid.uuid4().hex[:6].upper()}"
    return create_it_ticket(db, ticket_id, issue, priority)
