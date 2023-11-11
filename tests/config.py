from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.environ.get("BASE_URL")
URL_AUTH = os.environ.get("URL_AUTH")
URL_CATEGORY = os.environ.get("URL_CATEGORY")
URL_RECORD = os.environ.get("URL_RECORD")

TEST_USER_NAME = os.environ.get("TEST_USER_NAME")
TEST_USER_PASSWORD = os.environ.get("TEST_USER_PASSWORD")


