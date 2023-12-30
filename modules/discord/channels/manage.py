import discord

async def create_channel(channel_name: str, bot) -> discord.TextChannel:
    guild = bot.get_guild(1187236756236554330)

    # Create the channel
    channel = await guild.create_text_channel(channel_name, overwrites={
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)  
    })

    print(f"Created channel: {channel.name}")

    return channel

async def create_private_thread(thread_name: str, channel_id: int, member, bot) -> discord.Thread:
    channel = bot.get_channel(channel_id)

    # Create the thread
    thread = await channel.create_thread(
            name=thread_name,
            auto_archive_duration=60,
            type=discord.ChannelType.private_thread
    )
    await thread.add_user(member) # add user to thread
        
    print(f"Created new private thread: {thread.name}")
    return thread