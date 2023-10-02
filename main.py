import discord
from discord.ext import commands

# Initializing the command prefix of the bot to be /
client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("Im ready!!")
    print("----------------")

@client.command
async def test(ctx):
    await ctx.send("This is working")

client.run()






