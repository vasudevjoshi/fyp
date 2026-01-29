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
<<<<<<< HEAD
    prompt = f"""You are a chemical dermatologist with expertise in skincare ingredients and cosmetic chemistry.

Using the following context, identify the chemical compounds or active ingredients that can help resolve the given skin issue.
=======
    prompt = f"""
You are a chemical dermatologist with expertise in skincare ingredients and cosmetic chemistry.

Using the following context, identify and list the chemical compounds or active ingredients that can help resolve the mentioned skin issue.
>>>>>>> ac96cdff784083b19db79294680acedc2c79226b

Context:
{results}

Task:
<<<<<<< HEAD
Extract the relevant compounds/ingredients effective for the skin condition.
For each compound:
- Provide the compound name
- Provide a one-line explanation of why it is used (mechanism or benefit)

Return the response strictly in the following JSON format and nothing else:

{
  "skin_issue": "<skin issue from the query>",
  "recommended_compounds": [
    {
      "compound_name": "<name>",
      "reason": "<one-line explanation>"
    }
  ]
}
=======
Extract and list the relevant compounds/ingredients that are effective in treating or improving the condition described in the question. 
Provide the output as a clear bullet-point list with only compound names (no explanations).
>>>>>>> ac96cdff784083b19db79294680acedc2c79226b

Skin Issue:
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

