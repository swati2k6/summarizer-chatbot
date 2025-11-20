from transformers import pipeline
from utils import chunk_text_by_words, combine_summaries  # <-- IMPORTANT IMPORT

def get_summarizer(model_name: str):
    return pipeline(
        "summarization",
        model=model_name,
        tokenizer=model_name
    )

def summarize_long_text(summarizer, text: str, min_length: int = 150, max_length: int = 300):
    # 1. Break long text into chunks
    chunks = chunk_text_by_words(
        text,
        max_words=10000,
        chunk_words=1000,
        overlap_words=200
    )

    # 2. Summarize each chunk
    chunk_summaries = []
    for chunk in chunks:
        summary = summarizer(
            chunk,
            min_length=min_length,
            max_length=max_length,
            do_sample=False
        )[0]["summary_text"]
        chunk_summaries.append(summary)

    # 3. Combine summaries
    final_summary = combine_summaries(chunk_summaries)
    return final_summary
