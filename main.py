import asyncio
from telethon import TelegramClient
import itertools

# Your API credentials (replace with your own)
API_ID = '14011503'
API_HASH = '10f47cfbbcc7326db4365c54ca89e3df'

# Target bot's username (replace with the bot's username)
TARGET_BOT_USERNAME = 'URxFFBOT'

# File path for saving and reading codes
FILE_PATH = '4_letter_codes.txt'

# Initialize the Telegram client
client = TelegramClient('session_name', API_ID, API_HASH)

# Step 1: Generate all 4-letter codes and save to a text file
def generate_and_save_codes():
    codes_generator = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=4)
    with open(FILE_PATH, 'w') as file:
        for code in codes_generator:
            file.write(''.join(code) + '\n')

# Step 2: Read the codes from the file and send them to the bot
async def send_codes_from_file():
    with open(FILE_PATH, 'r') as file:
        codes = file.readlines()

    for code in codes:
        code = code.strip()  # Remove any trailing newline character
        await client.send_message(TARGET_BOT_USERNAME, "Gift Code 🎁")
        await asyncio.sleep(1)  # Wait for 1 second
        await client.send_message(TARGET_BOT_USERNAME, f"{code}")
        await asyncio.sleep(1)  # Wait for 1 second before sending the next code

async def main():
    # Step 1: Generate and save all the codes
    generate_and_save_codes()
    
    # Step 2: Send the codes from the text file
    async with client:
        await send_codes_from_file()

# Start the client
client.loop.run_until_complete(main())
