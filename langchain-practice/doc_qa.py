from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader

llm=Ollama(model="phi3")

loader=TextLoader("devops.txt")
docs=loader.load()

context=docs[0].page_content
question=input("Ask a question about DevOps: ")

prompt=f"""

Use the following context to answer the question:
Context: {context}
Question: {question}
"""
response=llm.invoke(prompt)
print("\n Answer: ", response)
