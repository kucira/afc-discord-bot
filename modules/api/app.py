def create_app(app_name, guide_description, member, supabase_instance):
    print("Creating new app...", app_name, guide_description, member.id)
    response = supabase_instance.table('applications').insert({
        "app_name" : str(app_name),
        "guide_description" : str(guide_description),
        "discord_user_id" : member.id,
    }).execute()

    return response