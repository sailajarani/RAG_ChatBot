from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

def get_completion(prompt, model="gpt-4o"):
    completion = client.chat.completions.create(model=model,messages=[
        {
            "role": "system",
            "content": "Your an AI assistant. "
        },
        {   "role": "user",
            "content": prompt,
        },],)
    return completion.choices[0].message.content