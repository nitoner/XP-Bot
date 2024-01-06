import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 

    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name="initroles", description="Initialize all roles")
    async def initialize_roles(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("You have permissions!")
        except: 
            await interaction.response.send_message("You don't have permissions!")


    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name='setcolor', description='Change color of role')
    @app_commands.describe(roles='Role to change', colors='Color to choose from')
    @app_commands.choices(roles=[
        discord.app_commands.Choice(name="0-9", value=1),
    ])
    @app_commands.choices(colors=[
        #discord.app_commands.Choice(name="Teal", value=discord.Color.blue()),
        discord.app_commands.Choice(name="Dark Teal", value=0x11806A)
    ])
    async def hello(self, interaction: discord.Interaction, 
                    colors: discord.app_commands.Choice[int],
                    roles: discord.app_commands.Choice[int]):
        await interaction.response.send_message("Hello World! Here is XP Bot!")


    @app_commands.command(name="test", description="A simple test")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here is a test!")


async def setup(bot):
    await bot.add_cog(Admin(bot))
