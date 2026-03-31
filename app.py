from src.loader import load_transcript
from src.splitter import split_text
from src.summarizer import summarize_chunks
from src.article_generator import generate_article
from utils.prompts import ARTICLE_PROMPT

import os

def main():
    url = input("Enter YouTube URL: ")

    print("\n[1] Loading transcript...")
    docs = load_transcript(url)

    print("[2] Splitting text...")
    chunks = split_text(docs)

    print("[3] Summarizing...")
    summary = summarize_chunks(chunks)

    print("[4] Generating article...")
    article = generate_article(summary, ARTICLE_PROMPT)

    os.makedirs("output", exist_ok=True)

    with open("output/article.md", "w") as f:
        f.write(article)

    print("\n Article saved to output/article.md")

if __name__ == "__main__":
    main()