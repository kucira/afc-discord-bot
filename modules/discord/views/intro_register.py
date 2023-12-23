import discord
from discord import ui

class IntroRegister(ui.View):

    def __init__(self):
        super().__init__()

    @ui.button(label="Register Application", style=discord.ButtonStyle.green)
    async def button1_callback(self, button, interaction):
        await interaction.response.send_message("Register application clicked!")

    @ui.button(label="Browse Application", style=discord.ButtonStyle.secondary)
    async def button2_callback(self, button, interaction):
        await interaction.response.send_message("Browse application clicked!")