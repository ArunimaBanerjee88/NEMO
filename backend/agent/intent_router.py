# backend/agent/intent_router.py

BANNED_KEYWORDS = [
    "sexy", "sex", "porn", "nude", "adult",
    "pregnant", "baby making", "children sex"
]

def detect_intent(message: str) -> str:
    msg = message.lower().strip()

    # 🚫 SAFETY FIRST
    for word in BANNED_KEYWORDS:
        if word in msg:
            return "unsafe"

    # 👋 Greeting
    if msg in ["hi", "hello", "hey"]:
        return "greeting"

    # 🧠 Learning intents
    if msg.startswith(("what is", "who is", "why", "how")):
        return "meaning"
    
    BANNED_KEYWORDS = [
    "sex", "sexy", "porn", "nude", "adult",
    "pregnant", "cocaine", "drug"
]

def detect_intent(message: str) -> str:
    msg = message.lower().strip()

    # SAFETY FIRST
    for word in BANNED_KEYWORDS:
        if word in msg:
            return "unsafe"

    if msg in ["hi", "hello", "hey"]:
        return "greeting"

    if msg.startswith(("what", "why", "how", "who", "when")):
        return "question"

    if "simplify" in msg:
        return "simplify"

    if "summary" in msg or "summarize" in msg:
        return "summarize"

    if "sound" in msg or "letter" in msg:
        return "phonics"

    return "general"
