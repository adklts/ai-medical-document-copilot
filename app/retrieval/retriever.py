import numpy as np
from app.processing.embeddings import embed_query
from app.processing.indexer import load_index

def retrieve_chunks(query: str, index_path: str, metadata_path: str, top_k: int = 3):
    index, metadata = load_index(index_path, metadata_path)
    query_vector = embed_query(query).reshape(1, -1)

    distances, indices = index.search(np.array(query_vector), top_k)

    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx])

    return results