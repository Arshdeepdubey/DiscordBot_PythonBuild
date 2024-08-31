from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Step 0 : Load the discord token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
# print(TOKEN)

# Step 1 : Simple bot setup
intents: Intents = Intents.default()
intents.message_content = True   #NOQA(No Quality Assurance)
client: Client = Client(intents=intents)

# Step 2 : Message Functionality
async def send_messages(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    # '?' implements the private message functionality, that the not will message you privately
    # is_private being walrus operator since after message, whatever the output results for the condition, will be stored in is_private
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Step 3 : Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!!')

# Step 4 : Handling Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_messages(message, user_message)


# Step 5 : Main Entry point
def main() -> None:
    client.run(token=TOKEN)

# Run the Bot and check functionality
if __name__ == '__main__':
    main()





