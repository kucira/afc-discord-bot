import discord
from discord import ui

class RegisterForm(ui.Modal, title="Register Form"):
    def __init__(self, member, bot):
        super().__init__()
        self.member = member
        self.bot = bot

        name = ui.TextInput(label='Name')
        answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)

        self.add_item(name)
        self.add_item(answer)
        
        async def on_submit(self, interaction: discord.Interaction):
            await interaction.response.send_message(f'Thanks for your response, {self.name}!', ephemeral=True)