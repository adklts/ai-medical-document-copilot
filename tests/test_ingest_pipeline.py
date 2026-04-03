from app.pipelines.ingest_pipeline import run_ingest_pipeline

result = run_ingest_pipeline(
    file_path="data/raw/Adrianne466_Jannie509_Simonis280_5b556a04-5899-ec90-f607-f125c7871e8f.txt",
    index_path="data/vectorstore/faiss_index.bin",
    metadata_path="data/vectorstore/metadata.pkl"
)

print(result)