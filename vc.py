import discord
from discord.ext import commands

@commands.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    embed = discord.Embed(title ="VC status", description=f'connected..',color = 0xF407A1)
    await ctx.send(embed = embed)
@commands.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    embed = discord.Embed(title ="VC status", description=f'left..',color = 0xF407A1)
    await ctx.send(embed = embed)