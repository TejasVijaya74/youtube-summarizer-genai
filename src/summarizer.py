from langchain_openai import OpenAI

def summarize_chunks(chunks):
    llm = OpenAI(temperature=0.3)

    summaries = []

    # Step 1: Summarize each chunk
    for chunk in chunks:
        prompt = f"""
        Summarize the following text in a concise way:

        {chunk.page_content}
        """
        summary = llm.invoke(prompt)
        summaries.append(summary)

    # Step 2: Combine summaries
    combined_text = " ".join(summaries)

    # Step 3: Final summary
    final_prompt = f"""
    Combine and refine the following summaries into a final coherent summary:

    {combined_text}
    """

    final_summary = llm.invoke(final_prompt)

    return final_summary