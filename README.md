# YouTube Summarizer → Article Generator (GenAI Project)

## Overview

This project is an end-to-end **Generative AI pipeline** that converts a YouTube video into a structured article. It extracts the video transcript, processes long content using chunking, generates concise summaries, and transforms them into a well-formatted article (Markdown/HTML).

---

##  Features

*  Extract transcript directly from YouTube videos
*  Handle long transcripts using intelligent chunking
*  Generate summaries using LLM (OpenAI)
*  Convert summaries into structured article format
*  Export output as Markdown and HTML

---

##  Problem Statement

Large YouTube videos generate transcripts that exceed the **LLM context window**, making it difficult to process the entire content at once.

---

##  Solution Approach

This project solves the problem using a **chunk-based Map-Reduce summarization pipeline**:

1. Split transcript into smaller chunks
2. Summarize each chunk independently (Map step)
3. Combine summaries into a final summary (Reduce step)
4. Convert final summary into a structured article

---

##  Architecture

```text
YouTube URL
   ↓
Transcript Loader
   ↓
Text Splitter (Chunking)
   ↓
Chunk-wise Summarization
   ↓
Final Summary (Reduce)
   ↓
Article Generator
   ↓
Markdown / HTML Output
```

---

##  Tech Stack

* Python
* LangChain Ecosystem

  * langchain-community
  * langchain-text-splitters
  * langchain-openai
* OpenAI LLM
* YouTube Transcript API
* Markdown

---

##  Project Structure

```bash
youtube-summarizer-genai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── summarizer.py
│   ├── article_generator.py
│
├── utils/
│   ├── prompts.py
│
└── output/
    ├── article.md
    ├── article.html
```

---

##  Installation

```bash
git clone https://github.com/your-username/youtube-summarizer-genai.git
cd youtube-summarizer-genai

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

##  Setup Environment Variables

### Windows (PowerShell)

```bash
setx OPENAI_API_KEY "your_api_key"
```

Restart terminal after setting the key.

---

##  Usage

```bash
python app.py
```

Then enter a YouTube URL when prompted.

---

##  Output

The system generates:

* `output/article.md` → Markdown article
* `output/article.html` → HTML version

---

##  Example Output Format

```markdown
# Title

## Introduction
Brief overview of the topic

## Key Insights
- Point 1
- Point 2
- Point 3

## Conclusion
Final summary and takeaways
```

---

##  Key Learning

* Handling long-context problems in LLMs
* Chunking strategies for scalable AI pipelines
* Map-Reduce pattern in Generative AI
* Prompt engineering for structured output

---

##  Future Improvements

* Streamlit UI for interactive usage
* PDF export functionality
* Multi-language support
* SEO optimization for generated articles
* Integration with vector databases (RAG)

---

##  One-Line Pitch

> Built a Generative AI pipeline that converts YouTube videos into structured articles using chunk-based summarization to overcome LLM context limitations.

---

##  Author

**Tejas V**
