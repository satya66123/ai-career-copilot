from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_ats_score(resume, job_description, strict_mode=True):
    embeddings = model.encode([resume, job_description])

    similarity = cosine_similarity(
        [embeddings[0]], [embeddings[1]]
    )[0][0]

    score = int(similarity * 100)

    return {"score": score}
