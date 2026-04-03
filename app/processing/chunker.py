from typing import List, Dict
from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP) -> List[Dict]:
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk
        })

        chunk_id += 1
        start += chunk_size - chunk_overlap

    return chunks