from transformers import pipeline

# Load model ONCE (important for performance)
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    max_new_tokens=180,
    do_sample=False,        # VERY IMPORTANT → no randomness
    temperature=0.7,
)

SYSTEM_PROMPT = (
    "You are NEMO, a kind and calm learning assistant for dyslexic children aged 4 to 12.\n"
    "Rules:\n"
    "- Use simple words\n"
    "- Short sentences\n"
    "- No adult topics\n"
    "- No jokes\n"
    "- Be educational and correct\n"
    "- If unsure, say you are unsure\n\n"
)

def generate_answer(user_question: str) -> str:
    prompt = (
        SYSTEM_PROMPT
        + f"Question: {user_question}\n"
        + "Answer:"
    )

    output = generator(prompt)[0]["generated_text"]

    # Clean output
    answer = output.split("Answer:")[-1].strip()

    # Stop runaway text
    answer = answer.split("\n")[0:5]
    answer = "\n".join(answer)

    return answer
