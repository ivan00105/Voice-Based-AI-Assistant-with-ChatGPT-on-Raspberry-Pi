import os
import openai
import asyncio
from src.translator import translate
from src.config import gpt_key

openai.api_key = gpt_key

async def gpt(prompt, lang):
    # Translate the prompt into English first for better accuracy
    if lang != "en-US":
        prompt = translate(prompt, "en")

    prompt = "Question: " + prompt + "\n"
    sys_content = ("Note that if you cannot answer the question or the query is about "
                   "something you do not know such as time-sensitive information(e.g. "
                   "today's weather/stock, .etc), your response can only contain \"IDK\" "
                   "even if the question is not in English(do not say something like As an AI language model...)")

    # Run the synchronous openai.ChatCompletion.create() in a separate thread
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_content},
            {"role": "user", "content": prompt}
        ]
    )
    return response