from transformers import pipeline
classifier =pipeline("sentiment-analysis")

result=classifier("Langchain is amazing for building apps")

print(result)
