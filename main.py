import discord
from discord.ext import commands
from kick import kick
import os
import openai
from dotenv import load_dotenv
from vc import join
from vc import leave
from openai import api_key
import nacl
import asyncio
from info import si
from uptime import uptime
from addrole import addrole
from banall import kickall
from banall import banall
# from music import play

load_dotenv()

# from music import play_song

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!!", intents=intents, help_command=None)
bot.add_command(kick)
bot.add_command(kickall)
bot.add_command(banall)
bot.add_command(join)
bot.add_command(leave)
bot.add_command(si)
bot.add_command(uptime)
bot.add_command(addrole)
# bot.add_command(play)

openai.api_key = os.getenv('openai') #needs openai token
completion = openai.Completion()

def Reply(question):
  prompt = f'You: {question}\n Bot: '
  response = completion.create(prompt=prompt,
                               engine="text-davinci-003", 
                               stop=['\You'],
                               max_tokens=200)
  answer = response.choices[0].text.strip()
  return answer

#ai chatbot function
@bot.command()
async def l(ctx, *, question):
   await ctx.send(Reply(question))


# bot.add_command(play_song)
@bot.command(name="hello")
@commands.is_owner()
async def responds_with_hi(ctx):
    await ctx.send("Hi")

#help command
@bot.command(name="help")
async def help(ctx):
    bot_name = ctx.bot.user.name
    bot_avatar = ctx.bot.user.avatar.url if ctx.bot.user.avatar else ctx.bot.user.default_avatar.url

    embed = discord.Embed(title=bot_name, color=discord.Color.blue())
    embed.set_author(name=bot_name, icon_url=bot_avatar)
    embed.set_footer(text=f"Use `{ctx.prefix}help <category>` for more info regarding a category.")

    embed.description = f"My prefix for this server is `{ctx.prefix}`.\nType `{ctx.prefix}help <category_name>` for more info on a command.\n"

    embed.add_field(name="Categories", value="• :crown: Owner\n• :shield: Moderation\n• :gear: Utility", inline=True)

    bot_info = f"Bot ID: {ctx.bot.user.id}\n"
    bot_info += f"Bot Owner: <@920601420812660746>\n"
    embed.add_field(name="Bot Info", value=bot_info, inline=True)

    await ctx.send(embed=embed)
    # embed = discord.Embed(title="Help",
    #                       description=f"This bot is a multi utiliy bot which also helps in moderation playing music and most of the work can be donned i can also chat with people of the server!! ",
    #                       color=0x7615D1)

#ping command
@bot.command(name="ping")
async def respond_with_ping(ctx):
    ping = bot.latency * 1000
    embed = discord.Embed(title="Ping", description=f"The ping of the bot is {ping:.2f}ms", color=0x7615D1)
    await ctx.send(embed=embed)

#will trigger the bot to reply on these messsages
@bot.event
async def on_message(msg):
    mention = msg.author.mention
    if msg.author.bot:
        return
    # if "hello" in msg.content.lower():
    #   await msg.channel.send(f"Hello {mention}")
    if "bsdk" in msg.content.lower():
        await msg.channel.send(f"Kya be {mention} lawde kya backchodhi krha hai madharchodh teri maiya choodh doonga ")
    if msg.content.lower() == "vanity":
        link = await msg.channel.create_invite(max_uses=0, max_age=0)
        await msg.channel.send(link)
    # if "<@920601420812660746>" in msg.content:
    #     await msg.channel.send(f"He is the almighty titty lover please wait he will reply!!!")
    if "<@1138086974343880734>" in msg.content :
       await msg.channel.send(f"Yes how may I help you ?")
    if "<@1138086974343880734> hello" in msg.content:
        await msg.channel.send(f"hi how are you ?{mention}")
    if "<@1138086974343880734> i am good wbu ?" in msg.content:
        await msg.channel.send(f"yeah i am also doing fine listning to mahesh dalle")
    if "<@1138086974343880734> call 11g officials" in msg.content:
        await msg.channel.send(f"<@&1120977070030344306>")
    # if "<@770857386343923732>" in msg.content :
    #   await msg.channel.send(f"That IITian is too busy to talk please don't bother him!!")
    await bot.process_commands(msg)

#will print in the terminal that the bot is alive
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="MAHESH DALLE"),
                              status=discord.Status.dnd)
    print(f"{bot.user.name}#{bot.user.discriminator} is alive now!!")

#Will count the no. of server it is in and will tell how many people it is watching over
@bot.command(name='sc')
async def server_count(ctx):
    members = sum(guild.member_count for guild in bot.guilds)
    embed = discord.Embed(title="Server Count",
                          description=f'I am in {len(bot.guilds)} servers and watching {members} members',
                          color=0xFF543A)
    await ctx.send(embed=embed)
    print(f'I am in {len(bot.guilds)} servers and watching {members} members')

#ban Function
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'The User has been banned')

#can DM the person present in the server
@bot.command()
@commands.has_permissions(administrator=True)
async def DM(ctx, user: discord.User, *, message):
    try:
        pass
        await user.send(message)
        embed = discord.Embed(title=DM, description=f'The message has been sent :smile:', color=0x7615D1)
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send('error')

#Message deleter
@bot.command()
async def clear(ctx, amount=0):
    if amount == 0:
        fail = await ctx.send("Please enter an amount to delete!")
        await asyncio.sleep(6)
        await fail.delete()

    if amount < 100:
        await ctx.channel.purge(limit=amount)
        sucess = await ctx.send(f"{amount} messages has been deleted :white_check_mark: ")  # sending success msg
        await asyncio.sleep(6)  # wait 6 seconds
        await sucess.delete()  # deleting the sucess msg

    else:
        if amount == 0:
            fail = await ctx.send("Please enter an amount to delete!")
            await asyncio.sleep(6)
            await fail.delete()

#avatar
@bot.command()
async def av(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar.url
    em = discord.Embed(color=discord.Color.from_rgb(255, 0, 0))
    em.set_image(url=f"{userAvatarUrl}")
    em.set_author(name=f"{avamember}")
    em.set_footer(text=f'Requested by {ctx.message.author}')
    await ctx.send(embed=em)

    
#Nuke
@bot.command()
@commands.has_permissions(administrator = True)
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None:
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.send("Nuked the Channel sucessfully!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")





bot.run(os.getenv('TOKEN'))
