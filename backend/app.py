from dotenv import load_dotenv
load_dotenv()

import os
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from google_auth import google_login, google_callback
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from fastapi import HTTPException
from pydantic import BaseModel
from database import init_db
from auth import login_user, register_user
from agent.agent import agent_response
from memory.chat_memory import get_chat_history, save_message
from fastapi import Request


app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", "dev-secret-key"),
    same_site="lax"
)
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

init_db()

class ChatInput(BaseModel):
    user_id: int
    message: str

class LoginInput(BaseModel):
    email: str
    password: str

class RegisterInput(BaseModel):
    email: str
    password: str


@app.post("/register")
def register(data: RegisterInput):
    user_id = register_user(data.email, data.password)
    if not user_id:
        raise HTTPException(400, "Email already exists")
    return {"user_id": user_id}

@app.post("/login")
def login(data: LoginInput):
    user_id = login_user(data.email, data.password)
    if not user_id:
        raise HTTPException(401, "Invalid credentials")
    return {"user_id": user_id}


@app.post("/chat")
def chat(data: ChatInput):
    save_message(data.user_id, "user", data.message)
    reply = agent_response(data.user_id, data.message)
    save_message(data.user_id, "assistant", reply)
    return {"reply": reply}

@app.get("/history/{user_id}")
def history(user_id: int):
    return get_chat_history(user_id)

@app.get("/auth/google")
async def auth_google(request: Request):
    return await google_login(request)

@app.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    return await google_callback(request)

@app.get("/")
def serve_login():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/chat.html")
def serve_chat():
    return FileResponse(FRONTEND_DIR / "chat.html")
