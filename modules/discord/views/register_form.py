import discord
from discord import ui
from modules.api import app
class RegisterForm(ui.Modal, title="Register Form"):
    name = ui.TextInput(label='Application Name')
    guide = ui.TextInput(label='Guide to test', style=discord.TextStyle.paragraph)

    def __init__(self, supabase_instance):
        super().__init__()
        self.supabase_instance = supabase_instance

    async def on_submit(self, interaction: discord.Interaction):
        try:
            app.create_app(self.name, self.guide, interaction.user, self.supabase_instance)
            await interaction.response.send_message(f'Thanks for your response, {self.name} {self.guide}!', ephemeral=True)    
        except Exception as e:
            print(e)