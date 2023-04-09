import asyncio
import json
from EdgeGPT import Chatbot, ConversationStyle

with open('./cookies.json', 'r') as f:
    cookies = json.load(f)

async def bing(prompt):
    bot = Chatbot(cookies=cookies)
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.balanced, wss_link="wss://sydney.bing.com/sydney/ChatHub")
    # close connection
    await bot.close()
    return response