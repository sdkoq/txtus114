import os

from os import environ

API_ID = int(os.environ.get('API_ID', '26441402'))
API_HASH = os.environ.get("API_HASH", "facbcdd5f6bf5802f13d470c10b0f473")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6782715381:AAHmURgZJjoeScU8ohUkepOKyd2DMBBSNA8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7120369395))

LOG = int(environ.get('LOG', '-1002047319861'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5374290660").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


