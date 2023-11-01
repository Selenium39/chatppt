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
         "content": '''你是一个为PowerPoint演示文稿提供建议的助手。回答时,请根据幻灯片数量为用户提供每张幻灯片的总结内容。有如下要求
                        1. 答案的语言必须为中文
                        2. 答案的格式必须为JSON数组对象,如下
                        [{“slide”:1,“title”:”xxxx”,”content”:”xxxx”,”keyword”:[“xxx”,”xxx”]},{“slide”:2,“title”:”xxxx”,”content”:”xxxx”,”keyword”:[“xxx”,”xxx”]}]
                        3. slide:幻灯片数量,title:幻灯片内容的标题,content:带有一些要点的内容,keyword:为每张幻灯片给出最能代表该幻灯片的最重要的关键词（不超过两个词）'''},
        {"role": "user", "content": user_message}
    ]


def generate_assistant_message(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    return response['choices'][0]['message']['content']
