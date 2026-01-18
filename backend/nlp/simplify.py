from transformers import pipeline

_simplifier = None

def get_simplifier():
    global _simplifier
    if _simplifier is None:
        _simplifier = pipeline(
            "text2text-generation",
            model="google/flan-t5-small"
        )
    return _simplifier

def simplify_text(text):
    simplifier = get_simplifier()
    prompt = f"Simplify for a dyslexic child:\n{text}"
    out = simplifier(prompt, max_length=100)
    return out[0]["generated_text"]
