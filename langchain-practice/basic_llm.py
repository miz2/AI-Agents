from langchain_community.llms import Ollama
llm=Ollama(model="phi3")

response=llm.invoke("Explain Devops in Simple words")
print(response)