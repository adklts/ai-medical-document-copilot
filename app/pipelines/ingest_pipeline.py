from app.ingestion.parser import extract_text
from app.ingestion.cleaner import clean_text
from app.processing.chunker import chunk_text
from app.processing.embeddings import embed_texts
from app.processing.indexer import build_faiss_index, save_index

def run_ingest_pipeline(file_path: str, index_path: str, metadata_path: str):
    raw_text = extract_text(file_path)
    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)

    texts = [chunk["text"] for chunk in chunks]
    embeddings = embed_texts(texts)

    index = build_faiss_index(embeddings)
    save_index(index, chunks, index_path, metadata_path)

    return {
        "num_chunks": len(chunks),
        "index_path": index_path,
        "metadata_path": metadata_path
    }