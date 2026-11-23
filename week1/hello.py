import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.environ["OPENROUTER_API_KEY"])

resp = client.chat.completions.create(
    model="openai/gpt-6-luna",
    messages=[{"role": "system", "content": "Tell me the meaning of life in one word"}],
)

print(resp.choices[0].message.content)

