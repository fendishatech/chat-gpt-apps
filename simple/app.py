# LIST ALL MODELS
# import os
# import openai

# openai.api_key = "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"
# # openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())


import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "how can i use .env files in python, do i have to install dotenv like package or nac i use os.getenv module, i am using pipenv",
        }
    ],
)

# print output
print(completion.choices[0].message.content)
