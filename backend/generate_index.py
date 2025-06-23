from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
import json

# Load features from JSON
with open("features.json", "r", encoding="utf-8") as f:
    features = json.load(f)

# Convert each feature into a Document object
docs = [
    Document(
        page_content=feature["description"],
        metadata={"title": feature["title"]}
    )
    for feature in features
]

# Set up embedding model
embedding = HuggingFaceEmbeddings()

# Create Chroma vector store and persist
db = Chroma.from_documents(docs, embedding, persist_directory="./chroma_db")
db.persist()

print("✅ Vector DB created and saved to chroma_db/")
