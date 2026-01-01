# PATH: api/api.py

from fastapi import FastAPI, Header
from pydantic import BaseModel
from uuid import uuid4
from supervisor.router import route_request
from db.base import SessionLocal

app = FastAPI(title="Agentic AI System")


class ChatRequest(BaseModel):
    message: str = "My laptop is not working"
    session_id: str | None = None


class ChatResponse(BaseModel):
    response: str
    session_id: str


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Agentic AI System is running. Visit /docs to test the API."
    }


@app.post("/chat", response_model=ChatResponse)
def chat(
    req: ChatRequest,
    x_user_id: str = Header(default="anonymous"),
    x_user_role: str = Header(default="user")
):
    session_id = req.session_id or str(uuid4())
    db = SessionLocal()

    try:
        response = route_request(
            db=db,
            message=req.message,
            session_id=session_id,
            user_id=x_user_id,
            user_role=x_user_role
        )
        return {"response": response, "session_id": session_id}
    finally:
        db.close()
