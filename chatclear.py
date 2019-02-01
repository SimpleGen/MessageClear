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
    print("ONLINE")

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Member")
    await bot.add_roles(member, role)
    

bot.run("NTQxMDE1NzA0OTg0NjE3MDEx.DzZUTA.pTnYdTKkRPxs78clH8s52W81y54")


