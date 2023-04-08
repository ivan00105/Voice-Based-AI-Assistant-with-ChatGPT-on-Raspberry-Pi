import os
import openai
from translator import translate
from config import gpt_key

openai.api_key = gpt_key


def gpt(prompt, lang):
    prompt = "Question: "+ prompt + "\n"
    sys_content = ''
    # if lang == "en-US":
    #     prompt = "Question:"+ prompt + "\n"
    #     # prompt += "Note that the question is in " 
    #     # prompt += "English." if lang=="en-US" else "Chinese." + "Your response should be in this language only if you do know the answer."
    #     # prompt += " However, if you cannot answer the question or the query is about something you do not know such as time-sensitive information, your response can only contain \"IDK\" even if the question is not in English."
    #     sys_content = " Note that if you cannot answer the question or the query is about something you do not know such as time-sensitive information(e.g. today's weather/stock, .etc), your response can only contain \"IDK\" even if the question is not in English(do not say something like As an AI language model...)"
    # else:
    #     prompt = "Question:"+ prompt + "\n"
    #     # prompt += "請注意，這問題是中文的。只有在您知道答案的情況下，才應使用中文回答。 但是，如果您無法回答問題或詢問的內容是您不了解的，例如時效性信息，即使問題不是英文，您的回答也只能包含 \"IDK\""
    #     sys_content = " Note that this question is in Chinese, that means your response should be in Chinese only if you can answer the question. If you cannot answer the question or the query is about something you do not know such as time-sensitive information(e.g. today's weather/stock, .etc), your response can just only contain \"IDK\" even if the question is not in English(do not say something like As an AI language model...)"

    print(prompt)
    sys_content = " Note that if you cannot answer the question or the query is about something you do not know such as time-sensitive information(e.g. today's weather/stock, .etc), your response can only contain \"IDK\" even if the question is not in English(do not say something like As an AI language model...)"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_content},
            {"role": "user", "content": prompt }
        ]
    )
    return response