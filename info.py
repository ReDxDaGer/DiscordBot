import discord
from discord.ext import commands

# This command provides the info of the bot that in how many server the bot is in and how many members in total it is watching
@commands.command(name='si', description='Get information about the server')
async def si(ctx):
    guild = ctx.guild
    embed = discord.Embed(title="Server Information", color=discord.Color.blue())
    embed.set_thumbnail(url=guild.icon)
    embed.set_author(name=f"{guild.name}'s Information", icon_url=ctx.bot.user.avatar.url)
    embed.set_footer(
        text=f'Requested by {ctx.message.author.name} • {ctx.message.created_at.strftime("%Y-%m-%d | %H:%M:%S")}',
        icon_url=ctx.author.display_avatar)

    bans_list = [entry.user async for entry in ctx.guild.bans()]
    embed.add_field(name="\n\n__About__",
                    value=f'**Name:** {guild.name}\n**ID:** {guild.id}\n**Owner:** {guild.owner.mention} :crown:\n**Created:** {guild.created_at.strftime("%Y-%m-%d | %H:%M:%S")}\n**Members:** {guild.member_count}\n**Banned:** {len(bans_list)}',
                    inline=False)

    embed.add_field(name="\n\n__Description__", value=f'> {guild.description}', inline=False)

    verification = guild.verification_level
    mfa = guild.mfa_level
    auth = (":x:" if 'disabled' in mfa else ":white_check_mark:" if 'require_2fa' in mfa else "Unknown")
    noti = guild.default_notifications.value
    notifications = ("Only mentions" if noti == 1 else "All messages")
    embed.add_field(name="\n\n__Additional__",
                    value=f'**Channels:** {len(guild.channels)}\n**Roles:** {len(guild.roles)}\n**Verification Level:** {str(verification).title()}\n**Upload Limit:** {"No Boosts Available" if "NitroBoost" not in guild.features else guild.max_upload_size}\n**Inactive Channel:** {guild.afk_channel.mention if guild.afk_channel else ":x:"}\n**System Messages Channel:** {guild.system_channel.mention if guild.system_channel else ":x:"}\n**Explicit Media Content Filter:** {":white_check_mark:" if guild.explicit_content_filter else ":x:"}\n**Boost Status:** {f"Level: {guild.premium_tier} [<a:boost:1138563557710114846> {guild.premium_subscription_count} boosts]" if guild.premium_tier > 0 else ":x:"}\n**2FA Requirement:** {auth}\n**Default Notifications:** {notifications}\n**Emojis:** {len(guild.emojis)}',
                    inline=False)

    await ctx.send(embed=embed)