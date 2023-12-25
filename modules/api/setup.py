import os
from modules import config
from supabase import create_client, Client, ClientOptions

config.load_env()

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10
))

def get_supabase() -> Client:
    return supabase