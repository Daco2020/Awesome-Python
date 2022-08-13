import os
from dotenv import load_dotenv

load_dotenv()


# API
APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
