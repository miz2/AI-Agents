from transformers import pipeline

summarizer = pipeline(
    "text2text-generation",
    model="facebook/bart-large-cnn"
)

text = """
DevOps is a culture and set of practices that combine software development and IT operations.
It aims to shorten the development lifecycle and deliver high-quality software continuously.
"""

result = summarizer("summarize: " + text, max_length=50, min_length=10)

print(result[0]["generated_text"])