# Civil AI Agent

A modular AI-driven assistant tailored for civil engineering use-cases leveraging interactive agents, RAG workflows, and LangGraph integration. Designed for rapid experimentation, deployment, and extension across research and production workflows.

---

## 🚀 Overview

The **Civil AI Agent** project is a full-stack AI assistant framework built using LangChain and LangGraph tools. It integrates FastAPI backend APIs, RAG (Retrieval-Augmented Generation), vector storage, frontend UI, and multi-agent support to help users interact with large civil engineering datasets and workflows in a meaningful, dynamic way.

This repository is structured to support modular tool integration, RAG pipelines, and plug-and-play AI agent workflows across use cases such as document analysis, knowledge search, and intelligent retrieval.

---

## ⭐ Features

- 🔍 **AI-Driven Retrieval & Search** – RAG integration with LangGraph & vector database support  
- 🧠 **Multi-Agent Support** – Orchestrate agent workflows for complex civil tasks  
- ⚡ **FastAPI Backend** – Production-ready API surface  
- 🌐 **Frontend UI** – Interactive user interface (Streamlit or equivalent)  
- 📦 **Modular & Extensible** – Easily add tools, prompts, and integrations  
- 🧪 **Pluggable Agents** – Support for custom LLM agents and tools

---

## 🧱 Architecture Diagram (Text)
                          ┌───────────────────────────┐
                          │        Frontend UI        │
                          │  (Streamlit / Web App)    │
                          └─────────────┬─────────────┘
                                        │
                                        │ HTTP Requests
                                        ▼
                          ┌───────────────────────────┐
                          │        FastAPI Server     │
                          │      (Backend Layer)      │
                          └─────────────┬─────────────┘
                                        │
                     ┌──────────────────┼──────────────────┐
                     │                  │                  │
                     ▼                  ▼                  ▼
         ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
         │   Agent Layer   │   │   RAG Pipeline  │   │  Tooling Layer  │
         │ (LangGraph)     │   │ (Retriever)     │   │ (Custom Tools)  │
         └────────┬────────┘   └────────┬────────┘   └────────┬────────┘
                  │                     │                     │
                  ▼                     ▼                     ▼
         ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
         │ Prompt Templates│   │  Vector Store   │   │ External APIs   │
         │ + Memory        │   │ (FAISS)         │   │ (Optional)      │
         └────────┬────────┘   └────────┬────────┘   └─────────────────┘
                  │                     │
                  ▼                     ▼
               ┌───────────────────────────────────────────┐
               │               LLM Provider                │
               │     (OpenAI / HuggingFace / Local LLM)   │
               └───────────────────────────────────────────┘


---

## 🛠️ Tech Stack

| Layer | Tool / Framework |
|-------|------------------|
| Backend | FastAPI, Uvicorn |
| AI | LangChain, LangGraph |
| Vector DB | FAISS (local) |
| LLM Providers | HuggingFace Hub / OpenAI |
| Frontend | Streamlit / Custom Web UI |
| Env Management | python-dotenv |
| Deployment | Docker, Cloud |

---

## 📥 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/bibas06/civil_ai_agent.git
   cd civil_ai_agent
2. **Create & activate virtualenv**
   ```bash
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
---

🔑 Environment Variables
# LLM API keys
OPENAI_API_KEY=your_openai_key
HF_API_TOKEN=your_huggingface_token

# Vector store config (if needed)
FAISS_PATH="./db/faiss_index"
