# PATH: tools/it_tools.py

from sqlalchemy.orm import Session
from db.repositories import save_it_ticket


def create_it_ticket(db: Session, ticket_id: str, issue: str, priority: str) -> str:
    save_it_ticket(db, ticket_id, issue, priority)

    return (
        "IT TICKET CREATED SUCCESSFULLY\n"
        f"ISSUE: {issue}\n"
        f"PRIORITY: {priority}\n"
        f"TICKET ID: {ticket_id}"
    )
