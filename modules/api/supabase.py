import os
from modules import config
from supabase import create_client, Client

config.load_env()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
user_email: str = os.getenv("SUPABASE_USER")
user_pass: str = os.getenv("SUPABASE_PASSWORD")

def get_supabase() -> Client:
  supabase: Client = create_client(url, key)
  return supabase

def sign_in_bot(supabase_instance):
  data = supabase_instance.auth.sign_in_with_password({
    "email": user_email,
    "password": user_pass 
  })

  # after login need set credentials session to postgres supabase
  # so postgres_client can read the RLS policy
  # issue with the supabase python client
  if data.user.id:
    session = supabase_instance.auth.get_session()
    handle_auth_change(supabase_instance, session)
    
  return data

# issue from the supabase python client
# https://github.com/supabase-community/supabase-py/discussions/391
# https://github.com/supabase-community/supabase-py/pull/370
def handle_auth_change(supabase, session): 
  postgrest_client = supabase.postgrest
  postgrest_client.auth(session.access_token)