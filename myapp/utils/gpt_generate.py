import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_development(user_message):
    conversation = build_conversation(user_message)
    try:
        assistant_message = generate_assistant_message(conversation)
    except openai.error.RateLimitError as e:
        assistant_message = "Rate limit exceeded. Sleeping for a bit..."

    return assistant_message


def build_conversation(user_message):
    return [
        {"role": "system",
         "content": "你是一个为PowerPoint演示文稿提供建议的助手。回答时，请根据幻灯片数量为用户提供每张幻灯片的总结内容。"
                    "答案的格式必须是： Slide X(the number of the slide): {title of the content} /n Content: /n 带有一些要点的内容"
                    "Keyword: /n 为每张幻灯片给出最能代表该幻灯片的最重要的关键词（不超过两个词）"},
        {"role": "user", "content": user_message}
    ]


def generate_assistant_message(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response['choices'][0]['message']['content']