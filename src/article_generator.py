from langchain_openai import OpenAI

def generate_article(summary, prompt_template):
    llm = OpenAI(temperature=0.5)

    prompt = prompt_template.format(summary=summary)

    return llm.invoke(prompt)