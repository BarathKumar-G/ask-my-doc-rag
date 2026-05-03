import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.ingestion.loader import load_documents
from app.ingestion.chunker import chunk_documents
from app.ingestion.embedder import generate_embeddings
from app.retrieval.retriever import store_embeddings


def main():
    # Resolve project root properly
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    folder_path = os.path.join(project_root, "data", "docs")

    # Phase 1
    docs = load_documents(folder_path)
    print(f"Loaded {len(docs)} document(s)")

    chunks = chunk_documents(docs)
    print(f"Generated {len(chunks)} chunk(s)")

    # Phase 2 (NEW)
    embeddings = generate_embeddings(chunks)
    print("Embeddings generated")

    store_embeddings(chunks, embeddings)


if __name__ == "__main__":
    main()