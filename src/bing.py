import asyncio
import json
from EdgeGPT import Chatbot, ConversationStyle

with open('./cookies.json', 'r') as f:
    cookies = json.load(f)

class Bing:
    def __init__(self):
        self.bot = Chatbot(cookies=cookies)

    async def bing(self, prompt):
        response = await self.bot.ask(prompt=prompt, conversation_style=ConversationStyle.balanced, wss_link="wss://sydney.bing.com/sydney/ChatHub")
        return response
    
    # close connection
    async def close(self):
        await self.bot.close()
        