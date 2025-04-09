from dotenv import load_dotenv
import os
import openai

load_dotenv()
OPENAI_API = os.getenv("OPENAI_API")

openai.api_key = OPENAI_API

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke about programmers."}
    ],
    temperature=0.7,
    max_tokens=100
)

print(response['choices'][0]['message']['content'])
