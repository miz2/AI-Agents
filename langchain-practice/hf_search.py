from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = [
    "Docker packages applications into containers",
    "Kubernetes orchestrates containers",
    "CI/CD automates deployments"
]

query = "How do we manage containers?"

docs_embeddings = model.encode(docs)
query_embedding = model.encode(query)

scores = util.cos_sim(query_embedding, docs_embeddings)

print("Similarity Scores:", scores)

best_match = scores.argmax()

print("\nBest Match:")
print(docs[best_match])