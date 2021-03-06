import discord
import logging
import os
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix='$', help_command=None)
token = os.environ['TOKEN_1']

@client.event
async def on_ready():
    await client.change_presence(
            status=discord.Status.idle, activity=discord.Game('VisualStudio Code'))
    print('online')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

for file in os.listdir('./commands'):

    if file.endswith('.py'):
        client.load_extension(f'commands.{file[:-3]}')

client.run(token)
