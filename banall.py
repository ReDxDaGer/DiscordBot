import discord
from discord.ext import commands

#This command can only be used the person who is having the ownership of the server for kicking all !!kickall  
@commands.command(name = "kickall",description="This command will abn all the  members in the server " )
@commands.is_owner()
async def kickall(ctx):
    await ctx.message.delete()
    await ctx.send("Kicking all member....")
    guild = ctx.guild
    for member in guild.members:
        try:
            await member.kick()
        except Exception as e:
            print(e)
            continue
# #This command can only be used the person who is having the ownership of the server for banning all !!banall  
@commands.command(name = "banall",description="This command will abn all the  members in the server " )
@commands.is_owner()
async def banall(ctx):
    await ctx.message.delete()
    await ctx.send("Banning all member....")
    guild = ctx.guild
    for member in guild.members:
        try:
            await member.ban()
        except Exception as e:
            print(e)
            continue