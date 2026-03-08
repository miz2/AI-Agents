from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm=Ollama(model="phi3")

template="""   
Explain the following concept in simple words: {concept}
"""

prompt=PromptTemplate(
    input_variables=["concept"],
    template=template
)

final_prompt=prompt.format(concept="Microsoft Azure")

response=llm.invoke(final_prompt)
print(response)