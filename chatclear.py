import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


prefix = "-"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Höher gewinnt")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def start(ctx):
    await bot.say(random.randint(0, 10000))

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("**DELETED**")

bot.run("NTM2MTQwNDIwNDI2NDk4MDc1.DySXNw.aTZWvdkLPmIUSEgdn2qOO91iYdo")


