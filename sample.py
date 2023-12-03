from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(secret)
client = OpenAI(
    api_key=str(os.getenv('OPENAI_API_KEY')),
)


def get_user_input():
    x = input("ask something\n")
    return x


def chatgpt_engiene(content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


do_you_want_to_continue = 1
while (do_you_want_to_continue == 1):
    content = get_user_input()
    answer = chatgpt_engiene(content)
    print(answer)
    do_you_want_to_continue = input("type 1 to continue")
    do_you_want_to_continue = int(do_you_want_to_continue)
