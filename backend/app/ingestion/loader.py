import os
from typing import List


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def load_documents(folder_path: str) -> List[str]:
    documents = []

    if not os.path.exists(folder_path):
        raise ValueError(f"Folder not found: {folder_path}")

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            text = load_txt(file_path)

            if text:  # skip empty files
                documents.append(text)

    return documents