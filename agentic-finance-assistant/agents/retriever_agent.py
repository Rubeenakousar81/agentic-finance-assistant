from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def retrieve_facts(query, index):
    return index.similarity_search(query, k=3)
