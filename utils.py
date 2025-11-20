import os
from typing import List

def read_text_file(path: str) -> str:
    path = os.path.expanduser(path)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_text_file(path: str, text: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def chunk_text_by_words(text: str, max_words: int = 8000, chunk_words: int = 1200, overlap_words: int = 200) -> List[str]:
    """Split `text` into chunks approximately `chunk_words` long with `overlap_words`."""
    words = text.split()
    if len(words) > max_words:
        words = words[:max_words]

    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_words, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        if end == len(words):
            break
        start = end - overlap_words
    return chunks

def combine_summaries(summaries: List[str]) -> str:
    return '\n\n'.join(summaries)

def load_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

