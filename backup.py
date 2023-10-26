import os
from telethon import TelegramClient
from googletrans import Translator


Channel = '@'
api_id = 
api_hash = ''

client = TelegramClient('anon', api_id, api_hash)
translator = Translator()

async def main():
    async for message in client.iter_messages(Channel, reverse=True):  # Iterate in reverse order
        print(f"Message ID: {message.id}")
        try:
            if message.media:
                path = await message.download_media()
        except:
            print("Error Dowloading")
   

            

with client:
    client.loop.run_until_complete(main())