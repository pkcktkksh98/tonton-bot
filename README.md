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

## 🚀 Getting Started

1. **Create Environment**:
   ```bash
   conda create -n tontonbot python=3.11
   conda activate tontonbot
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Generate FAISS Vector**:
   ```bash
   streamlit run app/ingest.py
   ```
   
3. **Run Streamlit App**:
   ```bash
   streamlit run app/run.py
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

## 📌 Notes

- This project assumes the model is downloaded from HuggingFace or accessible locally.
   
---    

## 🛡️ License

MIT License. Feel free to use and modify.
