from openai import OpenAI
import os
from dotenv import load_dotenv
from tools import search_web, extract_text_from_url

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_agent(topic):
    # Step 1: search web
    links = search_web(topic)

    if not links:
        return "No sources found."

    collected_text = ""

    # Step 2: extract text from top links
    for link in links[:3]:
        text = extract_text_from_url(link)
        if text:
            collected_text += text + "\n\n"

    if not collected_text:
        return "Could not extract content."

    # Step 3: send to LLM for final report
    prompt = f"""
You are an AI research assistant.

Create a structured research report on: {topic}

Use the provided web content to generate:
- Overview
- Key insights
- Important trends
- Conclusion

Web content:
{collected_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    report = response.choices[0].message.content
    return report