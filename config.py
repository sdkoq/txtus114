import os

API_ID = API_ID = 22609670

API_HASH = os.environ.get("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6739442523:AAHHA5HZmU6sqI-elmhTs8dwHqfhTizWwnQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5997896353))

LOG = -1002063321661

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5997896353").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


