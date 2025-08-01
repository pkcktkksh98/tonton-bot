
# Tonton FAQ Bot 🤖

This project is a chatbot that answers frequently asked questions about Tonton, a Malaysian streaming platform. It uses local LLM inference, FAISS-based retrieval, and a Streamlit UI.

---

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

### 🧠 Note on Model Files

If you're using a large `.gguf` model file and prefer not to copy it into the Docker image, mount the model directory at runtime:

```bash
docker run -p 8501:8501 -v ${PWD}/models:/app/models tonton-bot
```

If you're on Windows (CMD or PowerShell), use:

```cmd
docker run -p 8501:8501 -v D:\01_CodingProject\04_REV\models:/app/models tonton-bot
```

### ⚠️ Troubleshooting

- If Streamlit gives a "Runtime instance already exists!" error, make sure `app/run.py` **does not call** `stcli.main()` inside the script.
- Always access the app at `http://localhost:8501`, not `0.0.0.0`.

---

## 📁 Project Structure

```
.
├── Dockerfile
├── README.md
├── requirements.txt
├── app/
│   ├── run.py
│   ├── generator.py
│   ├── retriever.py
│   ├── interface.py
│   └── ingest.py
├── data/
│   └── tonton_faq.txt
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
└── models/
    └── your-model.gguf
```
