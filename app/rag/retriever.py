from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = None

def build_vectorstore(chunks):
    global vectorstore
    vectorstore = FAISS.from_texts(chunks, embeddings)

def retrieve(query: str):
    return vectorstore.similarity_search(query, k=4)
