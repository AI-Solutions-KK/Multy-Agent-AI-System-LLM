# PATH: tools/hr_tools.py

from sqlalchemy.orm import Session
from db.repositories import save_employee


def onboard_employee(db: Session, emp_id: str, name: str, role: str) -> str:
    save_employee(db, emp_id=emp_id, name=name, role=role)

    return (
        "EMPLOYEE ADDED SUCCESSFULLY\n"
        f"NAME: {name}\n"
        f"ROLE: {role}\n"
        f"ASSIGNED ID: {emp_id}"
    )
