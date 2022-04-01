import discord
import os
import praw
import random
from discord.ext import commands
from discord import FFmpegPCMAudio

client_secret = os.environ['CLIENT_SECRET']
client_id = os.environ['CLIENT_ID']
reddit_pass = os.environ['PASS']

reddit = praw.Reddit(

    check_for_async=False,
    client_id=client_id,
    client_secret=client_secret,
    username='Novax86',
    password=reddit_pass,
    user_agent="Server_Chan"

)

class MemeSender(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def donate(self, ctx):
        msg ='Server-Chan™ is a free and open source project and takes time and effort in order to develop, if you would like to support development send $5 to this link: https://rb.gy/enaq3a' 
        embed = discord.Embed(title='donate')
        embed.add_field(name='donations', value=msg, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        sub = reddit.subreddit('memes')
        hot = sub.hot(limit=50)
        random_post = []

        for submission in hot:
            random_post.append(submission)

        random_pick = random.choice(random_post)
        url = random_pick.url
        name = random_pick.title
        embed = discord.Embed(title=name)
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @commands.command()
    async def rickroll(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            vc = await channel.connect()
            source = FFmpegPCMAudio('./rick_roll.opus')
            vc.play(source)
        else:
            await ctx.send('You need to be in a voice channel to use this command')
    
    @commands.command() 
    async def scotland(self, ctx):
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            vc = await channel.connect()
            source = FFmpegPCMAudio('./scotland.m4a')
            vc.play(source)
        else:
            await ctx.send('You need to bee in a voice channel to use this command')

def setup(client):
    client.add_cog(MemeSender(client))
