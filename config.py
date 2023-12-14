from os import getenv

from dotenv import load_dotenv

load_dotenv()

DB_NAME = getenv("DB_NAME")
