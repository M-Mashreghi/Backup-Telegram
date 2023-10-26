import os
from telethon import TelegramClient
from googletrans import Translator
Channel = 
api_id = 
api_hash = ''

client = TelegramClient('anon', api_id, api_hash)
translator = Translator()

async def main():
    async for message in client.iter_messages(Channel, reverse=True): 
        print(f"Message ID: {message.id}")
        try:
            if message.media:
                if current_folder_name:
                    path = await message.download_media(current_folder_name)
                    print(f'Media saved to {path}')
                else:
                    print("No folder for media. Skipping media download.")
            else:
                text = message.text
                if text:
                    if translator.detect(text).lang == 'fa':
                        translation = translator.translate(text, src='fa', dest='en')
                        text = translation.text

                    current_folder_name = f'folder_{text}'  
                    os.makedirs(current_folder_name, exist_ok=True)
                    print(f'Created a folder for text: {current_folder_name}')
                else:
                    current_folder_name = None
        except:
            print("error")
            

with client:
    client.loop.run_until_complete(main())