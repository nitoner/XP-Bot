import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot 

        
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name="initroles", description="Initialize all roles")
    async def initialize_roles(self, interaction: discord.Interaction):
        await interaction.response.send_message("You have permissions!")



    @app_commands.command(name="hello", description="description")
    async def hello(self, interaction: discord.Interaction):    
        await interaction.response.send_message("Hello World! Here is XP Bot!")


    @app_commands.command(name="test", description="A simple test")
    async def test(self, interaction: discord.Interaction):    
        await interaction.response.send_message("Here is a test!")


async def setup(bot):
    await bot.add_cog(Admin(bot))
