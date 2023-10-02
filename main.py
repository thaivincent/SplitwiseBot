import discord
from discord.ext import commands

# Initializing the command prefix of the bot to be /

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot (command_prefix = '$', intents=intents)

@client.event
async def on_ready():
    print("Im ready!!")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("This is working")

client.run("MTE1ODIyMzIyMTQwMTg1NDAyMg.GsrmSZ.Ta2AjyKpmoxPJGLV9FNt5BKZxeALVZ30PJyg8o")






