import discord
from discord import ui

class IntroRegister(ui.View):

    def __init__(self):
        super().__init__()

    @ui.button(label="Register Application", style=discord.ButtonStyle.green)
    async def register_btn_callback(self, interaction: discord.Interaction, button: ui.Button):
        print("click register")
        await interaction.response.send_message("Register application clicked!")

    @ui.button(label="Browse Application", style=discord.ButtonStyle.secondary)
    async def browse_btn_callback(self, interaction: discord.Interaction, button: ui.Button):
        print("click browse")
        await interaction.response.send_message("Browse application clicked!")

