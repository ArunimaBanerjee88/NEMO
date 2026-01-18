from nlp.llm import llm_answer
from memory.chat_memory import save_message
from memory.user_state import get_user_state

BANNED = ["sex", "sexy", "porn", "nude", "drug", "cocaine"]

def safety_reply():
    return (
        "😊 Let’s keep learning safe and kind.\n"
        "We can talk about stars, animals, reading, or science.\n"
        "What would you like to learn?"
    )

def agent_response(user_id, user_message):
    msg = user_message.lower()

    for w in BANNED:
        if w in msg:
            reply = safety_reply()
            save_message(user_id, "assistant", reply)
            return reply

    level = get_user_state(user_id)

    reply = llm_answer(user_message, level)

    save_message(user_id, "assistant", reply)
    return reply
