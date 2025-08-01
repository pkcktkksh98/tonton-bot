from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def ingest_documents():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/distiluse-base-multilingual-cased-v2"
    )

    with open("data/tonton_faq.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.create_documents([raw_text])
    texts = [doc.page_content for doc in chunks]

    db = FAISS.from_texts(texts, embedding_model)
    db.save_local("faiss_index")
    print("DONE Generate")

if __name__ == "__main__":
    ingest_documents()
