import discord
import os
from modules import config
from modules.discord.views.intro_register import IntroRegister
from modules.api import setup

config.load_env()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv("BOT_TOKEN")

@client.event
async def on_ready() -> None:
    # bot ready and get the login user information and save to database
    print("successful login as {0.user}".format(client))

@client.event
async def on_member_join(member):
    data, count = setup.get_supabase().table('discord_users').insert({"discord_user_id": member.id, "discord_user_name": member.name}).execute()
    
        
@client.event  
async def on_member_remove(member):
    pass

@client.event
async def on_message(message: discord.Message) -> None:
    #check who sent the message
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('hello'):
        await message.channel.send("hello!")
    
    if message.channel.name == "info":
        # Add embed image
        embed = discord.Embed(title="My Title", description="My Description", color=0x0000FF)
        embed.set_image(url="https://example.com/image.png")

        intro_register = IntroRegister()
        await message.channel.send(embed=embed, view=intro_register)

client.run(token)
