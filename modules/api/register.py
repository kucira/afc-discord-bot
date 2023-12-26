def create_user(member, supabase_instance):
    response = supabase_instance.table('discord_users').select('*').eq('discord_user_id', member.id).execute()
    print(response.data)
    if response.data == []:
        response = supabase_instance.table('discord_users').insert({"discord_user_id": member.id, "discord_user_name": member.name}).execute()

    return response

def delete_user(member, supabase_instance):
    response = supabase_instance.table('discord_users').delete().eq('discord_user_id', member.id).execute()
    return response
