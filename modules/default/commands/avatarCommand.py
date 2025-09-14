import discord
from discord import app_commands
from discord.ext import commands

from Azurite import Logger
from Azurite import app
from Azurite.convert.image_to_link import image_to_link

class avatarCommand(commands.Cog):
    @app_commands.command(name='avatar', description='show user avatar')
    @app_commands.describe(member="chose a member")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.defer(thinking=True)

        embed = discord.Embed(
            title=f'{member.name} avatar!',
            description=" "
        )
        embed.set_image(url=member.avatar.url)

        await interaction.followup.send(embed=embed)
