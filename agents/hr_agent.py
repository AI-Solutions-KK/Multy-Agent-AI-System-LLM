# PATH: agents/hr_agent.py

from llm.client import GroqLLMClient
from tools.hr_tools import onboard_employee
from sqlalchemy.orm import Session
import uuid

llm = GroqLLMClient()


def hr_agent(db: Session, message: str) -> str:
    prompt = f"""
Extract employee name and role from the text.
Return STRICTLY in this format:
NAME=<name>
ROLE=<role>

Text:
{message}
"""

    response = llm.generate(prompt)

    name = ""
    role = ""

    for line in response.splitlines():
        if line.startswith("NAME="):
            name = line.replace("NAME=", "").strip()
        elif line.startswith("ROLE="):
            role = line.replace("ROLE=", "").strip()

    if not name or not role:
        return "Failed to extract employee details."

    emp_id = f"E-{uuid.uuid4().hex[:6].upper()}"
    return onboard_employee(db, emp_id, name, role)
