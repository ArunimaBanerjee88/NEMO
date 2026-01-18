from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text, top_k=5):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=top_k
    )
    tfidf = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out().tolist()
