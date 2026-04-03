import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
VECTORSTORE_PATH = os.getenv("VECTORSTORE_PATH", "data/vectorstore/faiss_index")
RAW_DATA_PATH = os.getenv("RAW_DATA_PATH", "data/raw")
PROCESSED_DATA_PATH = os.getenv("PROCESSED_DATA_PATH", "data/processed")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 800))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 150))
TOP_K = int(os.getenv("TOP_K", 3))