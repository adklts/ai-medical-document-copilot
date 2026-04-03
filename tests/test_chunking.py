from app.ingestion.parser import extract_text
from app.ingestion.cleaner import clean_text
from app.processing.chunker import chunk_text

file_path = "data/raw/Adrianne466_Jannie509_Simonis280_5b556a04-5899-ec90-f607-f125c7871e8f.txt"

text = clean_text(extract_text(file_path))
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")
print(chunks[0])