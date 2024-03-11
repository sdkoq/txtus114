import os

from os import environ

API_ID = int(os.environ.get('API_ID', '26441402'))
API_HASH = os.environ.get("API_HASH", "facbcdd5f6bf5802f13d470c10b0f473")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7029410461:AAGs1j7buK9kHEEBZbHUwFJR5L-rAiYiLTs")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7120369395))

LOG = int(environ.get('LOG', '-1001882447233'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7120369395").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


