# 🧠 Feature Discovery Assistant

A full-stack intelligent assistant built with **React**, **FastAPI**, and **GPT-3.5**, enabling users to query product features using natural language. The system uses vector similarity search for known features and seamlessly falls back to GPT when unfamiliar queries are asked — just like a real AI product assistant.

---

## 🚀 Project Highlights

* 🔍 **Semantic Search on Product Features**
  Uses ChromaDB and HuggingFace embeddings for fast retrieval of matching features.

* 🤖 **LLM Fallback via GPT-3.5**
  Automatically switches to OpenRouter’s GPT-3.5 when the vector store doesn’t return relevant matches.

* 💬 **Dynamic Chat History UI** *(in progress)*
  Inspired by ChatGPT — includes "New Chat" button and session-based memory (to be stored in backend).

* 🎨 **Modern Gradient UI**
  Clean dark theme with gradient background and visually clear role-based chat formatting.

---

## 🛠️ Tech Stack

* **Frontend**: React, JavaScript, HTML/CSS
* **Backend**: FastAPI (Python)
* **AI/LLM**: GPT-3.5 via OpenRouter API, LangChain, HuggingFace Embeddings
* **Vector Store**: ChromaDB
* **Other Tools**: dotenv, JSON for docs, CORS middleware

---

## 📁 Folder Structure

```
feature-discovery-assistant/
│
├── backend/
│   ├── main.py              # FastAPI server + GPT fallback logic
│   ├── features.json        # Feature data for vector search
│   ├── .env.example         # Sample env file for OpenRouter key
│   ├── requirements.txt     # Python dependencies
│   └── chroma_db/           # Auto-generated vector store
│
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── App.css          # UI styling (dark theme)
│   └── public/
│
└── README.md                # You're here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/feature-discovery-assistant.git
cd feature-discovery-assistant


### 2. Backend Setup
```
bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python generate_index.py
cp .env.example .env            # Add your API key here
uvicorn main:app --reload
```

### 3. Frontend Setup
```
bash
cd frontend
npm install
npm start
```

---

## 🔐 Environment Variables

In the backend/ directory, create a .env file with this key:


OPENROUTER_API_KEY=sk-or-your-key-here


**Do not share your `.env` file publicly.** Use `.env.example` to show the required format.

---

## 🧪 How It Works

* Ask a product-related question like:
  *"How to enable dark mode?"* → System fetches the matched feature from vector DB.

* Ask something not present in the docs:
  *"How to contact customer support?"* → The assistant replies using GPT fallback.

Each bot response shows the **source feature title** (if from vector DB) or indicates it’s a **GPT fallback**.

---

## ✅ Sample Use Cases

| User Prompt                   | Source                       |
| ----------------------------- | ---------------------------- |
| How to enable notifications?  | Retrieved from features.json |
| What if I forgot my password? | Answered via GPT fallback    |
| How to disable analytics?     | Retrieved from vector store  |
| Can I change the language?    | Answered via GPT fallback    |

---

## 📌 Why This Project Matters

This project reflects real-world applications of:

* Generative AI with **GPT-3.5 + RAG pipelines**
* Vector search with **LangChain + ChromaDB**
* Hands-on **frontend/backend integration**
* Clean, deployable, and scalable architecture

It’s a great fit for internships or roles involving LLMs, agents, and product engineering.

---

## 📦 Requirements


# requirements.txt

fastapi
uvicorn
langchain
openai
chromadb
huggingface_hub
python-dotenv
pydantic
tqdm


---

## 📬 Contact

**Author**: Adityan Nambiar
**Email**: adityannambiar9@gmail.com
**LinkedIn**:- linkedin.com/in/adityannambiar/
**GitHub**: github.com/AdityanNambiar/

---

> ⭐ Star this repo if you found it useful, and feel free to fork or contribute!

---

