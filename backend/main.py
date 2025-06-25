import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

embedding = HuggingFaceEmbeddings()
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)
retriever = db.as_retriever(search_kwargs={"k": 5})

@app.post("/ask")
async def ask_question(query: Query):
    try:
        results = db.similarity_search_with_score(query.question, k=3)
        relevant_docs = [doc for doc, score in results if score < 0.75 and len(doc.page_content) > 30]

        if relevant_docs:
            context = "\n\n".join([doc.page_content for doc in relevant_docs])
            matched_title = relevant_docs[0].metadata.get("title", "Unknown")

            prompt = f"""Use the following product feature descriptions to answer the question.
If the answer isn't in the context, just say "Sorry, I can only help with product features."

Context:
{context}

Question: {query.question}
Answer:"""

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content.strip()
            return {
                "answer": answer,
                "source": matched_title + " (📄 From Docs)"
            }

        else:
            fallback_prompt = f"""You are a helpful AI assistant. Answer the following question even if it’s unrelated to product features.

Question: {query.question}
Answer:"""

            response = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=[{"role": "user", "content": fallback_prompt}]
            )
            answer = response.choices[0].message.content.strip()
            return {
                "answer": answer,
                "source": "💬 ChatGPT Fallback"
            }

    except Exception as e:
        return {
            "answer": f"❌ Error: {str(e)}",
            "source": "None"
        }
