import discord
from discord import app_commands
from discord.ext import commands

class banCommand(commands.Cog):
    def __init__(self, app):
        self.app = app
        super().__init__()
    @app_commands.command(name='ban', description='ban a member')
    @app_commands.describe(user='chose user', reason='reason')
    async def ping(self, interaction: discord.Interaction, user: discord.Member, reason: str = None):
        await interaction.response.defer(thinking=True)
        if not interaction.user.guild_permissions.ban_members:
            await interaction.followup.send(f"``❌`` You do not have sufficient permissions to use this.")
            return
        await user.ban(reason=reason)
        await interaction.followup.send(f'Banned {user.mention}. Reason: {reason}')
