import discord
import time as t
from discord.ext import commands

initialTime = t.time()


@commands.command(name='uptime', description = 'Shows the uptime of the discord bot ')
@commands.has_permissions(administrator = True)
async def uptime(ctx):
  currentTime= t.time()
  seconds = int(currentTime - initialTime)
  minutes = seconds//60
  hours = minutes //60
  days = hours // 24
  embed = discord.Embed(title=":green_circle: Uptime",description=f'```{days}d {hours-days*24}h {minutes-hours*60}m {seconds-minutes*60}s```',color=0x71F707)
  await ctx.send(embed= embed)