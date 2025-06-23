from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Load vectorstore from disk
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="chromadb_store", embedding_function=embedding)

# Choose your LLM (use OpenAI if you get credits, or HF fallback)
use_openai = False

if use_openai:
    from langchain.chat_models import ChatOpenAI
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
else:
    from langchain.llms import HuggingFaceHub
    pipe = pipeline("text2text-generation", model="google/flan-t5-large", max_length=512)
    llm = HuggingFacePipeline(pipeline=pipe)


# Build QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

# Ask a question
while True:
    query = input("\nAsk a question about your product features (or type 'exit'): ")
    if query.lower() == "exit":
        break

    answer = qa.run(query)
    print("\n🤖 Assistant:\n", answer)
