import discord
from discord.ext import commands
import youtube_dl

@commands.command()
async def play(ctx, url):
    # Check if the author is in a voice channel
    if ctx.author.voice is None:
        await ctx.send("You are not in a voice channel.")
        return

    # Check if the bot is in a voice channel
    if ctx.voice_client is None:
        await ctx.send("I am not in a voice channel. Use !join to invite me.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    ctx.voice_client.stop()
    ctx.voice_client.play(discord.FFmpegPCMAudio(url2, executable="ffmpeg"))