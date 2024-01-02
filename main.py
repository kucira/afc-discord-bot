import discord
import os
from modules import config
from modules.discord.views.intro_register import IntroRegister
from modules.discord.views.register_form import RegisterForm
from modules.api import supabase
from modules.api import register
config.load_env()

intents = discord.Intents.all()
bot = discord.Client(intents=intents)
token = os.getenv("BOT_TOKEN")
supabase_instance = supabase.get_supabase()
res = supabase.sign_in_bot(supabase_instance)

@bot.event
async def on_ready() -> None:
    # bot ready and get the login user information and save to database
    print("bot successful login as {0.user}".format(bot))
    # if res.user.id:
    #     print(res.user)
    #     guild = bot.get_guild(1187236756236554330)
    #     async for member in guild.fetch_members(limit=None):
    #         if not member.bot:
    #             user = register.create_user(member, supabase_instance)
    #             print(user)

@bot.event
async def on_member_join(member):
    # Add user to database
    user = register.create_user(member, supabase_instance)
    print("add user", user)


@bot.event  
async def on_member_remove(member):
    # Remove user from database
    user = register.delete_user(member, supabase_instance)
    print("delete user", user)

@bot.event
async def on_message(message: discord.Message) -> None:
    #check who sent the message
    if message.author == bot.user:
        return
    msg = message.content
    if msg.startswith('hello'):
        await message.channel.send("hello!")
    
    if message.channel.name == "info":
        # Add embed image
        embed = discord.Embed(title="My Title", description="My Description", color=0x0000FF)
        embed.set_image(url="https://example.com/image.png")

        intro_register = IntroRegister(member=message.author, bot=bot)
        await message.channel.send(embed=embed, view=intro_register)

bot.run(token)
