import discord
from discord.ext import commands
import config


# Setting permissions of the bot
intents = discord.Intents.all()

# Initializing the command prefix of the bot to be $
client = commands.Bot (command_prefix = '$', intents=intents)

@client.event
async def on_ready():
    global server_guild
    global member_list

    # where server_guild is a class(Guild) and represents the server.
    server_guild = client.get_guild(config.guild_id)

    # This is a list of "Member" objects
    member_list = server_guild.members

    print("Im ready!!")
    print("----------------")

@client.command()
async def hello(ctx):
    await ctx.send("This is working")

@client.command()
async def list_members(ctx):
    exclusive_id = discord.utils.get(server_guild.roles, name="Splitwise")
    # Adding all of the names of server members into a list
    name_list = []
    for member in member_list:
        if exclusive_id in member.roles:
            name_list.append(member.name)
    await ctx.send(str(name_list)[1:-1])
        
client.run(config.token)