# LexiBot: Local LLM Streamlit FAQ Assistant

LexiBot is a lightweight FAQ assistant built using a locally hosted LLM model (`Nous-Hermes-2-Mistral-7B-DPO`) and a Streamlit frontend interface. It leverages HuggingFace's Transformers and supports context-based generation for Tonton-like services.

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
├── models/                   # Place for downloaded models (if needed)
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
   conda create -n lexibot python=3.10
   conda activate lexibot
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Streamlit App**:
   ```bash
   streamlit run app/interface.py
   ```

---

## 📦 Requirements

```
transformers
torch
streamlit
```

(Optional: `accelerate`, `sentencepiece` if required by model)

---

## 📌 Notes

- This project assumes the model is downloaded from HuggingFace or accessible locally.
- Add future enhancements like FAISS, context loaders, or RAG pipelines in `data/`.

---

## 🛡️ License

MIT License. Feel free to use and modify.