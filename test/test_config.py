import os
from dotenv import load_dotenv

load_dotenv()


SECRET_ENV = os.getenv("SECRET_ENV")
API_KEY = os.getenv("API_KEY")
print(SECRET_ENV)