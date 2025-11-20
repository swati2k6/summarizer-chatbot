from summarizer import get_summarizer, summarize_long_text
from utils import load_file

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python cli.py <path_to_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Load document
    text = load_file(filepath)

    # Create summarizer model
    summarizer = get_summarizer(model_name="facebook/bart-large-cnn")

    # Create summary
    summary = summarize_long_text(
        summarizer=summarizer,
        text=text,
        min_length=150,
        max_length=300
    )

    print("\n=== SUMMARY ===\n")
    print(summary)

