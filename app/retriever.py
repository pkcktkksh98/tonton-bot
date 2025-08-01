from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings as HFEmbeddingsWrapper  # fallback if needed

def get_embedding_model():
    model_name = "sentence-transformers/distiluse-base-multilingual-cased-v2"
    model = SentenceTransformer(model_name)
    return HuggingFaceEmbeddings(model_name=model_name)
    # Or if it fails: return HFEmbeddingsWrapper(model_name=model_name)

def get_relevant_docs(query: str):
    embedding_model = get_embedding_model()
    db = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)
    docs = db.similarity_search(query)
    return docs
