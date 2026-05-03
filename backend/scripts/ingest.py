import sys
import os

# Fix import path (important for your structure)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_documents


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    folder_path = os.path.join(project_root, "data", "docs")

    docs = load_documents(folder_path)
    print(f"Loaded {len(docs)} document(s)")

    chunks = chunk_documents(docs)
    print(f"Generated {len(chunks)} chunk(s)\n")

    for i, chunk in enumerate(chunks[:5]):
        print(f"Chunk {i+1}:\n{chunk}\n{'-'*40}")


if __name__ == "__main__":
    main()