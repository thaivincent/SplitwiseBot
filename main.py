import discord
from discord.ext import commands
import config
import json

# Setting permissions of the bot
intents = discord.Intents.all()

# Initializing the command prefix of the bot to be $
client = commands.Bot (command_prefix = '$', intents=intents)

# This class represents the running balance of everybody in the server.
# the ith bal coresponds to the ith person in the memberlist, excluding yourself.
# This is custom tailored to my server of 7 people. (yeah this is trash)

class Balance:
    def __init__(self,bal1,bal2,bal3,bal4,bal5,bal6):
        self.bal1 = bal1
        self.bal2 = bal2
        self.bal3 = bal3
        self.bal4 = bal4
        self.bal5 = bal5
        self.bal6 = bal6
    
    # A function which returns the total balance you owe to everyone.
    def totbal(self):
        return self.bal1 + self.bal2 + self.bal3 + self.bal4 + self.bal5 + self.bal6
    



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
    print(name_list)


        
client.run(config.token)