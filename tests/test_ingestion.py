from app.ingestion.parser import extract_text
from app.ingestion.cleaner import clean_text

# 👉 Use ONE of your files here
file_path = "data/raw/Adrianne466_Jannie509_Simonis280_5b556a04-5899-ec90-f607-f125c7871e8f.txt"

raw_text = extract_text(file_path)
cleaned_text = clean_text(raw_text)

print("RAW TEXT (first 500 chars):")
print(raw_text[:500])

print("\nCLEANED TEXT (first 500 chars):")
print(cleaned_text[:500])