import os
from telethon import TelegramClient
from datetime import datetime
Channel = 
api_id = 
api_hash = ''

client = TelegramClient('anon', api_id, api_hash)

async def main():
    async for message in client.iter_messages(Channel):
        print(f"Message ID: {message.id}")
        if message.date:
            # Create a directory structure based on the message date and time
            date_time = message.date
            directory_path = f"{date_time:%Y-%m-%d %H-%M}"
            os.makedirs(directory_path, exist_ok=True)

        if message.photo:
            # Download photos
            path = await message.download_media(file=directory_path)
            print(f'Photo saved to {path}')
        elif message.video:
            # Download videos
            path = await message.download_media(file=directory_path)
            print(f'Video saved to {path}')
        elif message.file:
            # Download files
            path = await message.download_media(file=directory_path)
            print(f'File saved to {path}')
        elif message.audio:
            # Download audio
            path = await message.download_media(file=directory_path)
            print(f'Audio saved to {path}')

with client:
    client.loop.run_until_complete(main())