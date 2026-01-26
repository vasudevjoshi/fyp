import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# PHI_API_KEY = os.getenv("PHI_API_KEY")
# PHI_API_URL = os.getenv("PHI_API_URL")

from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# headers = {
#     "Authorization": f"Bearer {PHI_API_KEY}",
#     "Content-Type": "application/json"
# }
def generate_response(results, query):
    prompt = f"""
Use the following context to answer the question.

Context:
{results}

Question:
{query}
"""
    return ask_llm(prompt)



def ask_llm(prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return completion.choices[0].message.content

