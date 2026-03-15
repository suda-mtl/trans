import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-67b47bbff8134add99108d538629f886",
    base_url="https://api.deepseek.com")

system_message="""

"""

user_message = """
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ],
    stream=False
)

print(response.choices[0].message.content)