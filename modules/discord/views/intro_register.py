import discord
from discord import ui
from modules.discord.channels import manage
from modules.discord.views.register_form import RegisterForm

class IntroRegister(ui.View):
    def __init__(self, member, bot, supabase_instance):
        super().__init__()
        self.member = member
        self.bot = bot
        self.supabase_instance = supabase_instance

    @ui.button(label="Register Application", style=discord.ButtonStyle.green)
    async def register_btn_callback(self, interaction: discord.Interaction, button: ui.Button):
        print("click register")
        # channel = discord.utils.get(self.bot.get_all_channels(), name="info")
        # thread = await manage.create_private_thread(self.member.name, channel.id, self.member, self.bot)
        # await thread.send("Please register your application")
        # await interaction.response.send_message("Check your notification to register you application")
        
        register_form = RegisterForm(supabase_instance=self.supabase_instance)
        await interaction.response.send_modal(register_form)
        # await thread.send(view=register_form)

    @ui.button(label="Browse Application", style=discord.ButtonStyle.secondary)
    async def browse_btn_callback(self, interaction: discord.Interaction, button: ui.Button):
        print("click browse")
        await interaction.response.send_message("Browse application clicked!")

