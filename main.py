import discord
from discord.ext import commands
import config
import json

# Importing the current balance information via the JSON file
bal_file = open('balances.json')

balance_dict = json.load(bal_file)

# Setting permissions of the bot
intents = discord.Intents.all()

# Initializing the command prefix of the bot to be $
client = commands.Bot (command_prefix = '$', intents=intents)

# A function which gets the payee list of the member, which is the namelist without the specified member.
def get_payee_list (member_name):
    payee_list = name_list[:]
    payee_list.remove(member_name)
    return payee_list


# A function which takes in a valid member and payee, and outputs the index of that payee relative to the member
# Each payess index is determined by the member list order with the member itself removed.

def get_index (member, payee):
    index = 0
    for name in get_payee_list(member):
        if name == payee:
            return index
        else: index += 1



@client.event
async def on_ready():
    global server_guild
    global member_list
    global name_list

    # where server_guild is a class(Guild) and represents the server.
    server_guild = client.get_guild(config.guild_id)

    # This is a list of "Member" objects
    member_list = server_guild.members

    #Creating a member list of all included splitwise members
    exclusive_id = discord.utils.get(server_guild.roles, name="Splitwise")

    # Adding all of the names of server members into a list
    name_list = []
    for member in member_list:
        if exclusive_id in member.roles:
            name_list.append(member.name)

    print("Im ready!!")
    print("----------------")

# A function which takes in the member name and tries to find them in the member list, returns the member if found, false otherwise 

def get_member (member_name):
    for member in member_list:
        # Check if the member's username or display name matches the provided name
        if member.name == member_name or member.display_name == member_name:
            return member

    return False
    

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

@client.command()
async def totalbal(ctx):
    message_content = ctx.message.content.split()
    member_name = message_content[-1]

    tot = 0
    member = get_member(member_name)
    if member:
        member_name = member.name
        if member_name in balance_dict["balance"]:
            member_balances = balance_dict["balance"][member_name] # member_balances is list of tuples where each tuple represents a balance
            for balance in member_balances.items():
                tot += balance[-1]
            await ctx.send(f"Total Owed: ${tot}")    
        else:
            await ctx.send(f"No balance data found for {member_name}")
    else:
        await ctx.send("Please specify a valid member.")

@client.command()
async def bal(ctx):
    message_content = ctx.message.content.split()
    member_name = message_content[-1]
    member = get_member(member_name)
    if member:
        member_name = member.name
        if member_name in balance_dict["balance"]:
            member_balances = balance_dict["balance"][member_name] # member_balances is list of tuples where each tuple represents a balance
            index = 0
            payee_list = get_payee_list(member_name)
   
            for balance in member_balances.items():
                await ctx.send(f"{payee_list[index]}: ${balance[-1]}")
                index += 1
               
        else:
            await ctx.send(f"No balance data found for {member_name}")
    else:
        await ctx.send("Please specify a valid member.")
    


@client.command()
async def pay(ctx, payee: commands.MemberConverter, ammount_payed):
    member = ctx.Author
    member_name = member.name
    if payee:
        payee_name = payee.name
        payee_index = get_index(member_name)
        if member_name in balance_dict["balance"]:
            member_balances = balance_dict["balance"][member_name] # member_balances is list of tuples where each tuple represents a balance
            if (member_balances[payee_index][-1] - ammount_payed) >= 0:
                payee_balance = member_balances[payee_index][-1]
                payee_balance -= ammount_payed
                await ctx.send(f"The ammount of {ammount_payed} was sucessfully payed to {payee_name}. Your new outstanding balance is: {payee_balance}.")
            else:
                difference = ammount_payed - payee_balance
                await ctx.send(f"The ammount you are trying to pay is {difference} more than what you owe them, try again.")
        else: 
            await ctx.send(f"No balance data found for {member_name}")
    else:
        await ctx.send("Please specify a valid member.")


@client.command()
async def debug(membername):
    member = get_member(membername)

client.run(config.token)