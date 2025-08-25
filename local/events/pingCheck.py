import discord
from discord.ext import tasks,commands

def pingCheck(bot: commands.Bot,
              interval, Round,
              Logger):
    @tasks.loop(seconds=interval)
    async def pingCheckTask():
        latency = round(bot.latency * 1000, Round)
        Logger.INFO(f"Ping: {latency} ms")
    return pingCheckTask
