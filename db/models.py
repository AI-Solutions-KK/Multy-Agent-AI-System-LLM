# PATH: db/models.py

from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from db.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    emp_id = Column(String, unique=True, index=True)
    name = Column(String)
    role = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class ITTicket(Base):
    __tablename__ = "it_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String, unique=True, index=True)
    issue = Column(Text)
    priority = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    sender = Column(String)  # USER / ASSISTANT
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
