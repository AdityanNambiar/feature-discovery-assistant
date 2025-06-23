# Run this script to generate vector index (chroma_db/) from features.json

# generate_index.py
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import JSONLoader

embedding = HuggingFaceEmbeddings()
loader = JSONLoader(file_path="features.json", jq_schema=".features[]", text_content=False)
docs = loader.load()
db = Chroma.from_documents(docs, embedding, persist_directory="./chroma_db")
db.persist()
print("✅ Vector DB created and saved to chroma_db/")
