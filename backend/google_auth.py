from fastapi import Request
from fastapi.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth
from database import get_db
import os

print("GOOGLE_CLIENT_ID =", os.getenv("GOOGLE_CLIENT_ID"))
print("GOOGLE_CLIENT_SECRET =", os.getenv("GOOGLE_CLIENT_SECRET"))


oauth = OAuth()

oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

async def google_login(request: Request):
    redirect_uri = "http://127.0.0.1:8000/auth/google/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = token.get("userinfo")

    if not user:
        return RedirectResponse("http://127.0.0.1:5500/index.html")

    email = user["email"]
    google_id = user["sub"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE email=?", (email,))
    row = cur.fetchone()

    if row:
        user_id = row[0]
    else:
        cur.execute(
            "INSERT INTO users (email, google_id) VALUES (?, ?)",
            (email, google_id)
        )
        conn.commit()
        user_id = cur.lastrowid

    conn.close()

    return RedirectResponse(
        f"http://127.0.0.1:8000/chat.html?user_id={user_id}"
    )
