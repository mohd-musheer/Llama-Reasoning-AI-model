# 🧠 Reasoning Llama AI

A reasoning-focused local LLM chat application powered by Quantized Llama 3, llama.cpp, FastAPI, and Docker.

It runs fully locally using GGUF models and provides a modern ChatGPT-style interface with markdown and LaTeX rendering support.


---

## 🚀 Demo Features

- ⚡ Quantized GGUF Llama 3 inference
- 🧠 Reasoning-focused prompting
- 🦙 llama.cpp backend
- ⚙️ FastAPI API server
- 🎨 Modern responsive UI
- ✍️ Markdown rendering
- ➗ LaTeX math rendering
- 🐳 Dockerized deployment
- 💻 CPU inference support
- 🔄 Streaming-ready architecture

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Backend |
| FastAPI | API framework |
| llama.cpp | Local LLM inference |
| Docker | Containerization |
| JavaScript | Frontend |
| HTML/CSS | UI |
| Jinja2 | Templates |

---

# 📂 Project Structure

```text
reasoning-llama-ai/
│
├── app/
│   ├── api.py
│   ├── static/
│   └── templates/
│
├── model/
│   └── llama3-q4_k_m.gguf
│
├── Dockerfile
├── start.sh
├── requirements.txt
└── README.md
```

---

# 🐳 Docker Hub

Docker Image:

```text
mohdmusheer/reasoning-llama-ai
```

Docker Hub Link:

```text
https://hub.docker.com/r/mohdmusheer/reasoning-llama-ai
```

Pull image directly:

```bash
docker pull mohdmusheer/reasoning-llama-ai:latest
```

---

# ⚙️ Run Locally

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mohd-musheer/Llama-Reasoning-AI-model.git

cd Llama-Reasoning-AI-model
```

---

## 2️⃣ Build Docker Image

```bash
docker build -t reasoning-llama-ai .
```

---

## 3️⃣ Run Container

```bash
docker run -p 8000:8000 reasoning-llama-ai
```

---

# 🌐 Open Application

```text
http://localhost:8000
```

---

# 📡 API Endpoint

## POST `/generate`

### Request

```json
{
  "prompt": "Explain machine learning simply."
}
```

### Response

```json
{
  "input": "Explain machine learning simply.",
  "response": "Machine learning is..."
}
```

---

# 🧠 Model

This project uses:

- Quantized GGUF Llama 3 model
- llama.cpp inference backend

---

# 📌 Notes

- Optimized for CPU inference
- Works on low-memory systems
- Fully local deployment
- Docker-ready architecture
- Streaming support can be added later

---

# 🔮 Future Improvements

- Real-time token streaming
- Conversation memory
- RAG integration
- Multi-model support
- GPU acceleration
- Authentication
- Persistent chat history

---

# 📜 License

MIT License