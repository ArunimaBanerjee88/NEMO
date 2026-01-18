def adapt_level(text):
    length = len(text.split())
    if length < 20:
        return "easy"
    elif length < 60:
        return "medium"
    return "hard"
