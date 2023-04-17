import os
import openai
import asyncio
from src.translator import translate
from src.config import gpt_key

sys_content = ("Note that if you cannot answer the question which is about "
                   "something you do not know such as time-sensitive information(e.g. "
                   "today's weather/stock, .etc), you can only reply \"IDK\" in your response without other characters."
                   "Do not say something like As an AI language model..., I'm sorry... and etc.")

class ChatGPT:
    def __init__(self):
        openai.api_key = gpt_key
        self.messages = [
            {"role": "system", "content": sys_content},
        ]

    async def gpt(self, prompt, lang):
        #translate the prompt into English first for better accuracy
        if lang != "en-US":
            prompt = translate(prompt, "en")

        prompt += "\n"
        self.messages.append({"role": "user", "content": prompt})
        #run the synchronous openai.ChatCompletion.create() in a separate thread
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role":"assistant", "content": response['choices'][0]['message']["content"]})
        return response

#Test

# chat_gpt = ChatGPT()
# async def main():
#     # Call the gpt() method with the query and language
#     gpt_response = await chat_gpt.gpt("What's the weather today", "en-Us")
#     gpt_response = await chat_gpt.gpt("I mean in Hong Kong", "en-Us")
# if __name__ == "__main__":
#     asyncio.run(main())