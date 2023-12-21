import discord
import os
from modules import config

config.load_env()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
token = os.getenv("CLIENT_TOKEN")

@client.event
async def on_ready() -> None:
    # bot ready and get the login user information and save to database
    print("successful login as {0.user}".format(client))

@client.event
async def on_message(message: discord.Message) -> None:
    #check who sent the message
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('hello'):
        await message.channel.send("hello!")
    
    if message.channel.name == "general":
        # Add embed image
        embed = discord.Embed(title="My Title", description="My Description", color=0x0000FF)
        embed.set_image(url="https://example.com/image.png")

        # Add button
        button = discord.ui.Button(label="My Button", url="https://example.com/")

        # Add view
        view = discord.ui.View()
        view.add_item(button)

        # Send the message
        await message.channel.send(embed=embed, view=view)

client.run(token)
