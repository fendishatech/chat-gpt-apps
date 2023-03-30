import os
from dotenv import load_dotenv
import openai


#  Load .env variables
load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

messages = []
system_msg = input("What type of chatbot would you like to create? \n")
messages.append({"role": "system", "content": system_msg})


print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
