from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Docker containerizes applications",
    "Kubernetes manages containers"
]

embeddings = model.encode(sentences)

print(embeddings)