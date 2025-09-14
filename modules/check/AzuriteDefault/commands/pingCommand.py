import discord
from discord import app_commands
from discord.ext import commands

class pingCommand(commands.Cog):
    def __init__(self, app):
        self.app = app
        super().__init__()
    @app_commands.command(name='ping', description='ping')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.defer(thinking=True)
        latency = self.app.latency
        await interaction.followup.send(f"Pong! ``{latency}`` ms")