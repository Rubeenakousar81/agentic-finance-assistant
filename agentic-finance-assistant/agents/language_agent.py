from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def generate_summary(query, retriever):
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
    return qa.run(query)
