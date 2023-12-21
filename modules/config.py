import os
from dotenv import load_dotenv

def load_env():
    """
    Loads environment variables from .env file
    """
    load_dotenv()

    required_vars = {
        "CLIENT_TOKEN",
    }

    for var in required_vars:
        if var not in os.environ:
            raise KeyError(f"{var} not found in environment variables")