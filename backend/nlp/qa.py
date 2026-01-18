from transformers import pipeline

_qa = None

def get_qa():
    global _qa
    if _qa is None:
        _qa = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )
    return _qa

def answer_question(question: str, level="easy"):
    qa = get_qa()

    prompt = (
        "Answer simply for a dyslexic child.\n"
        f"Question: {question}\n"
        "Answer:"
    )

    out = qa(prompt, max_length=80)
    return out[0]["generated_text"]
