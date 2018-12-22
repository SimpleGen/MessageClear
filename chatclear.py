import discord
from discord.ext import commands

TOKEN = ""
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("bot online.")

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("DELETED")

client.run("NTI1OTMzNjE0NjQzMjgxOTMx.Dv91aA.xtpbWF1-fA8xRTiy7GVe7de4w9E")
