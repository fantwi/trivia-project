from dotenv import load_dotenv
import os
load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
TEST_DB_NAME = os.environ.get("TEST_DB_NAME")