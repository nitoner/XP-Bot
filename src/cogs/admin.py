import discord
import sys
from src.database import Database
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    
    DEFAULT_ROLES = [('0-9', 'Novice'), ('10-19', ''), ('20-29', ''), 
                          ('30-39', ''), ('40-49', '', ''), ('50-59', '', ''), (), ()]

    def __init__(self, bot):
        self.bot = bot 

    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name='initroles', description='Initialize all roles')
    async def initialize_roles(self, interaction: discord.Interaction):
        """
        TODO: test if none admin can use this command
        """
        db = Database()
        connection = await db.get_connection()
        print(db)
        #check if table roles in db is empty
        #for i in range, 
        #   create role, store id in db


    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.command(name='setcolor', description='Change color of role')
    @app_commands.describe(roles='Role to change', 
                           colors='Color to choose from')
    @app_commands.choices(roles=[
        discord.app_commands.Choice(name='0-9', value=0),
    ])
    @app_commands.choices(colors=[
        discord.app_commands.Choice(name='Teal', value=0x1ABC9C)
    ])
    async def set_color(self, interaction: discord.Interaction, 
                    colors: discord.app_commands.Choice[int],
                    roles: discord.app_commands.Choice[int]):
        await interaction.response.send_message(f'Changing role {roles.value} to color {colors.value}')


    @app_commands.command(name="test", description="A simple test")
    async def test(self, interaction: discord.Interaction):
        await interaction.response.send_message("Here is a test!")


async def setup(bot):
    await bot.add_cog(Admin(bot))
