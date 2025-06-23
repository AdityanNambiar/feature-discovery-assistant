import json
import os
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from dotenv import load_dotenv

# Load environment variables (optional for future use)
load_dotenv()

# Load JSON data
with open("features.json", "r") as f:
    features = json.load(f)

# Prepare documents for embedding
docs = []
for feature in features:
    text = f"Title: {feature['title']}\nDescription: {feature['description']}\nSteps: {' → '.join(feature['steps'])}"
    docs.append(Document(page_content=text, metadata={"title": feature["title"]}))

# Split text if needed
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Use HuggingFace embeddings (FREE & offline)
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Embed and store into ChromaDB
vectorstore = Chroma.from_documents(
    documents=split_docs,
    embedding=HuggingFaceEmbeddings(),
    persist_directory="./chroma_db"
)
vectorstore.persist()

print("✅ Features embedded and stored in ChromaDB.")
