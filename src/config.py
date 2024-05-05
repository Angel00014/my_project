from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
SECRET = os.environ.get("SECRET")
IMPORT_RECORDS_SYSTEM_ONE_MOCK = os.environ.get("IMPORT_RECORDS_SYSTEM_ONE_MOCK")
ID_IMPORT_CATEGORY = os.environ.get("ID_IMPORT_CATEGORY")

BOOTSTRAP_URL = os.environ.get("BOOTSTRAP_URL")
TOPIC = os.environ.get("TOPIC")
