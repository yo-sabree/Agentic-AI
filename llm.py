from langchain_community.llms import Ollama


def generate_content(topic, keywords,trending):
    llm = Ollama(model="llama3.2:latest")

    prompt = f"""
    Write an engaging, SEO-optimized blog post on '{topic}'.
    **Important:**
    - Use these **SEO keywords**: {', '.join(keywords)}
    - Mention **trending topics**: {', '.join(trending)}
    - Do not force them, use them when needed.
    - Humanize the content and Give as final output.
    Ensure:
    - Focus on readability and user engagement rather than overusing keywords
    - Make it **friendly and natural** (like a human conversation)
    - Use **short and simple sentences**.
    - Incorporate storytelling or real-world examples for engagement
    - Short, easy-to-read paragraphs with clear subheadings
    - The content should not exceed 500 words
    - Use very simple words, day to day words and normal grammer like how humans talks.
    """

    response = llm.invoke(prompt)
    return response.strip()