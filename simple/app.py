import os
from dotenv import load_dotenv
import openai


#  Load .env variables
load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

query = input("What do you like chat gpt to answer for you :")

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": query,
        }
    ],
)

# print output
print(completion.choices[0].message.content)
