from app.pipelines.qa_pipeline import run_qa_pipeline

result = run_qa_pipeline(
    query="What is the diagnosis?",
    index_path="data/vectorstore/faiss_index.bin",
    metadata_path="data/vectorstore/metadata.pkl"
)

print("ANSWER:")
print(result["answer"])