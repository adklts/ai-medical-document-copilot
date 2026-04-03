import xml.etree.ElementTree as ET
from pathlib import Path

input_folder = "data/raw_xml"
output_folder = "data/raw"

Path(output_folder).mkdir(parents=True, exist_ok=True)

for file in Path(input_folder).glob("*.xml"):
    try:
        tree = ET.parse(file)
        root = tree.getroot()

        text = ""

        for elem in root.iter():
            if elem.text and elem.text.strip():
                text += elem.text.strip() + "\n"

        output_file = Path(output_folder) / (file.stem + ".txt")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Converted: {file.name}")

    except Exception as e:
        print(f"Error in {file.name}: {e}")

print("Done!")