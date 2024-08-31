import discord
from discord.ext import commands
import json

#load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']

#create an instance of a client
intents = discord.Intents.default()
intents.members = True # Enable member intents
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)

# event: on_ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# event: on_message
@client.event
async def on_message(message):
    # prevent bot from responding to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# run the bot
client.run(TOKEN)