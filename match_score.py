from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resumes, job_desc):
    texts = resumes + [job_desc]
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(texts)
    scores = cosine_similarity(tfidf[:-1], tfidf[-1:])
    return scores.flatten()
