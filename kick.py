import discord
from discord.ext import commands

#This command is used for kicking members of the server you just have to write !!kick @mention user
@commands.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """Kick User from the server"""
    await member.kick(reason=reason)
    if reason is not None:
        await member.send(f"You have been kicked from {ctx.guild.name} for {reason}")
    else:
        await member.send(f"You have been kicked from {ctx.guild.name}")

    await ctx.send(f"{member.mention} has been kicked")

#This command is used for banning members of the server you just have to write !!ban @mention user
@commands.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):

    await member.ban(reason=reason)
    if reason is not None:
        await member.send(f"You have been banned from {ctx.guild.name} for {reason}")
    else:
        await member.send(f"You have been banned from {ctx.guild.name}")
    await ctx.send(f"{member.mention} has been banned")
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.channel.send("Please mention atleast one member")
    else:
        await ctx.send(str(error))


