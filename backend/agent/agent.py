from memory.user_state import get_user_state, update_user_state
from agent.planner import decide_next_task
from memory.chat_memory import save_message
from agent.intent_router import detect_intent
from nlp.simplify import simplify_text
from nlp.summarize import summarize_text


def agent_response(user_id, user_message):
    letter, stage = get_user_state(user_id)
    intent = detect_intent(user_message)

    save_message(user_id, "user", user_message)

     # 🚫 SAFETY RESPONSE (NEW)
    if intent == "unsafe":
        reply = (
            "😊 Let’s keep our learning safe and kind.\n"
            "We can talk about stars, animals, reading, or science.\n"
            "What would you like to learn today?"
        )

    elif intent == "greeting":
        reply = "Hi 😊 I’m Nemo. I’m here to help you learn calmly."

    elif intent == "greeting":
        reply = "Hi 😊 What would you like to learn today?"

    elif intent == "simplify":
        reply = simplify_text(user_message)

    elif intent == "summarize":
        reply = summarize_text(user_message)

    elif intent == "phonics":
        reply, next_stage = decide_next_task(letter, stage)
        update_user_state(user_id, letter, next_stage)

    else:
        reply = "That’s okay 😊 Tell me what you want help with."

    save_message(user_id, "assistant", reply)
    return reply
