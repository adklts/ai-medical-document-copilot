from app.retrieval.retriever import retrieve_chunks

results = retrieve_chunks(
    query="What is the diagnosis?",
    index_path="data/vectorstore/faiss_index.bin",
    metadata_path="data/vectorstore/metadata.pkl",
    top_k=3
)

for r in results:
    print("=" * 50)
    print(r["text"])