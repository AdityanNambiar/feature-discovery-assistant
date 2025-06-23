from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import json

embedding = HuggingFaceEmbeddings()

with open("features.json", "r", encoding="utf-8") as f:
    data = json.load(f)

docs = [
    {
        "page_content": feature["description"],
        "metadata": {"title": feature["title"]}
    }
    for feature in data
]

db = Chroma.from_documents(
    documents=[doc["page_content"] for doc in docs],
    embedding=embedding,
    metadatas=[doc["metadata"] for doc in docs],
    persist_directory="./chroma_db"
)

db.persist()
print("✅ Vector DB created and saved to chroma_db/")
