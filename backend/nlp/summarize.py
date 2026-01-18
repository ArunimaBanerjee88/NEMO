from transformers import pipeline

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )
    return _summarizer

def summarize_text(text):
    if len(text.split()) < 40:
        return text

    summarizer = get_summarizer()
    out = summarizer(text, max_length=80, min_length=30)
    return out[0]["summary_text"]
