from langchain_community.document_loaders import TextLoader
loader=TextLoader("devops.txt")
documents=loader.load()
print(documents)