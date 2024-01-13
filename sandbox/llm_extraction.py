from dotenv import load_dotenv

from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

template = """ 
#TASK: Extract the relationship in a triple way (Sujeto-predicado-objeto) from the following text
"""  # noqa: E501

prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])


# Function definition
model = ChatOpenAI()
chain = prompt | model

if __name__ == '__main__':
    response = chain.invoke({"input":"In this paper we provide a comprehensive introduction to knowledge graphs, which have recently garnered significant attention from both industry and academia in scenarios that require exploiting diverse, dynamic, large-scale collections of data. After some opening remarks, we motivate and contrast various graph-based data models and query languages that are used for knowledge graphs. We discuss the roles of schema, identity, and context in knowledge graphs. We explain how knowledge can be represented and extracted using a combination of deductive and inductive techniques. We summarise methods for the creation, enrichment, quality assessment, refinement, and publication of knowledge graphs. We provide an overview of prominent open knowledge graphs and enterprise knowledge graphs, their applications, and how they use the aforementioned techniques. We conclude with high-level future research directions for knowledge graphs. "})
    print(response)
