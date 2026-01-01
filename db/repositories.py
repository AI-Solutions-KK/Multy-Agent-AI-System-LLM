# PATH: db/repositories.py

from sqlalchemy.orm import Session
from db.models import Employee, ITTicket, ChatSession
from datetime import datetime


def save_employee(db: Session, emp_id: str, name: str, role: str):
    employee = Employee(emp_id=emp_id, name=name, role=role)
    db.add(employee)
    db.commit()


def save_it_ticket(db: Session, ticket_id: str, issue: str, priority: str):
    ticket = ITTicket(
        ticket_id=ticket_id,
        issue=issue,
        priority=priority
    )
    db.add(ticket)
    db.commit()


def save_chat_message(db: Session, session_id: str, sender: str, message: str):
    chat = ChatSession(
        session_id=session_id,
        sender=sender,
        message=message,
        created_at=datetime.utcnow()
    )
    db.add(chat)
    db.commit()


def get_last_messages(db: Session, session_id: str, limit: int = 5):
    return (
        db.query(ChatSession)
        .filter(ChatSession.session_id == session_id)
        .order_by(ChatSession.created_at.desc())
        .limit(limit)
        .all()
    )
