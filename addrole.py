import discord
from discord.ext import commands
@commands.command()
@commands.has_permissions(administrator = True)
async def addrole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    em = discord.Embed(title="Role adding", description = f'The role has been added', colour=0x07ECF7)
    await ctx.send(embed =em)