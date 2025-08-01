# Local LLM Streamlit FAQ Assistant

TontonBot is a lightweight FAQ assistant built using a locally hosted LLM model (`Nous-Hermes-2-Mistral-7B-DPO`) and a Streamlit frontend interface. It leverages HuggingFace's Transformers and supports context-based generation for Tonton-like services.

---

## ✅ Features

- Local LLM inference using Transformers (no internet needed after setup)
- Short or long responses based on context (not forced to use max tokens)
- Simple Streamlit UI for input/output
- Modular code structure (easy to extend with RAG, embeddings, etc.)

---

## 📁 Project Structure

```
lexibot_llm_streamlit/
│
├── app/
│   ├── interface.py          # Streamlit frontend
│   └── generator.py          # Model loading and answer generation
│                 
├── data/                     # Placeholder for data context or FAISS/RAG
│
├── .gitignore
├── README.md
└── requirements.txt
```
---

## 🧱 System Architecture
```
                                        ┌──────────────────────────────┐
                                        │       Offline Preprocess     │
                                        │  (generate FAISS embeddings) │
                                        └─────────────┬────────────────┘
                                                      │
                                     ┌──────────────────────────────────────┐
                                     │     1. Generate FAISS Vector Index   │
                                     │     - Using sentence-transformers    │
                                     │     - distiluse-base-multilingual    │
                                     └─────────────────┬────────────────────┘
                                                       │
                                  ┌────────────────────▼───────────────────────┐
                                  │           2. Run Streamlit App             │
                                  │  - Loads FAISS index and metadata          │
                                  │  - Loads HuggingFace model:                │
                                  │    Nous-Hermes-2-Mistral-7B-DPO            │
                                  └────────────────────┬───────────────────────┘
                                                       │
                                               User Query Input
                                                       │
                                          ┌────────────▼────────────────┐
                                          │    Semantic Embedding       │
                                          │ (same embedding model used) │
                                          └────────────┬────────────────┘
                                                       │
                                          ┌────────────▼───────────────┐
                                          │    FAISS Vector Search     │
                                          └────────────┬───────────────┘
                                                       │
                                          ┌────────────▼────────────────┐
                                          │ HuggingFace Transformer LLM │
                                          │  (Nous-Hermes-2-Mistral-7B) │
                                          └────────────┬────────────────┘
                                                       │
                                                Final Response
```
---

## 🚀 Getting Started

1. **Create Environment**:
   ```bash
   conda create -n tontonbot python=3.11
   conda activate tontonbot
   cd tontonbot
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Generate FAISS Vector**:
   ```bash
   python app/ingest.py
   ```
   
## 🐳 Docker Setup

You can containerize and run the Tonton FAQ Bot using Docker with the following steps:

### 📦 1. Build the Docker Image

Make sure you're in the root project directory (same level as the `Dockerfile`), then run:

```bash
docker build -t tonton-bot .
```

### ▶️ 2. Run the Container

```bash
docker run -p 8501:8501 tonton-bot
```

Once running, open your browser and go to:

```
http://localhost:8501
```

---

## 📦 Requirements

```
langchain
faiss-cpu
transformers
sentence-transformers
streamlit
torch
PyMuPDF
llama-cpp-python
tiktoken
sentencepiece
llama-index
langchain-community
```

(Optional: `accelerate`, `sentencepiece` if required by model)

---

# 📋 Example Questions That Can Be Asked

- Kenapa lepas bayar aku tak boleh tengok cerita?
- Aku dah langgan, tapi kenapa masih keluar iklan?
- Macam mana nak batal langganan TontonUp setiap bulan?
- Macam mana nak tukar password?
- Boleh tak aku langgan kalau aku kat luar Malaysia?
- Kenapa keluar error masa aku tengok Tonton?
  
---

## 📌 Notes

- This project assumes the model is downloaded from HuggingFace or accessible locally.
   
---    

## 🛡️ License

MIT License. Feel free to use and modify.
