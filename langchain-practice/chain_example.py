from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="phi3")

prompt = PromptTemplate(
    input_variables=["Tool"],
    template="What is {Tool} in DevOps?"
)

chain = prompt | llm

response = chain.invoke({"Tool": "Terraform"})

print(response)