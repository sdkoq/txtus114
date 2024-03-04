import os

from os import environ

API_ID = int(os.environ.get('API_ID', '25339665'))
API_HASH = os.environ.get("API_HASH", "979cab179b80d3a826a27ab0c16dcc4a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6320511438:AAHhA0AVfWPLAuKVnc7HGHzxpEmYZILh6rU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5997896353))

LOG = int(environ.get('LOG', '-1001699267852'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5997896353").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


