import discord
from discord.ext import tasks,commands

def pingCheck(bot: commands.Bot,
              interval,
              Logger):
    @tasks.loop(seconds=interval)
    async def pingCheck():
        latency = bot.latency * 1000
        Logger.INFO(f"Ping: {latency} ms")
    return pingCheck()
