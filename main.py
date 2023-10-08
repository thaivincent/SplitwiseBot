import discord
from discord.ext import commands
import config


# Setting permissions of the bot
intents = discord.Intents.all()

# Initializing the command prefix of the bot to be $
client = commands.Bot (command_prefix = '$', intents=intents)


@client.event
async def on_ready():
    # where server_guild is a class(Guild) and represents the server.
    server_guild = client.get_guild(config.guild_id)
    # This is a list of "Member" objects
    global member_list 
    member_list = server_guild.members

    print("Im ready!!")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("This is working")

@client.command()
async def list_members(ctx):
    # Adding all of the names of server members into a list
    name_list = []
    for i in member_list:
        name_list.append(i.name)

        
    

client.run(config.token)