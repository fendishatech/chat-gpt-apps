import os
import openai
import gradio
from dotenv import load_dotenv


#  Load .env variables
load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

messages = [
    {
        "role": "system",
        "content": "You are a senior software developer",
    }
]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(
    fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro"
)

demo.launch(share=True)
