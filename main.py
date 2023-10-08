import discord
from discord.ext import commands
import config

# Initializing the command prefix of the bot to be $

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot (command_prefix = '$', intents=intents)

role_exclude =  discord.utils.get()

# Initialize the list of members in the group
group_list=[]
members = ctx.guild.members

for i in members:
    group_list.append(i.name)
    print("added:" + i.name)

@client.event
async def on_ready():
    print("Im ready!!")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("This is working")

@client.command()
async def list_members(ctx):
    await ctx.send("List of members:")
    await ctx.send(",".join(group_list))

client.run(config.token)