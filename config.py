import os

from os import environ

API_ID = int(os.environ.get('API_ID', '25957229'))
API_HASH = os.environ.get("API_HASH", "f19e0303f0d218f1744a28b826b7dc96")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6711385952:AAHh6_HrAFPU6qZeYXfXv__CDt-v2EdJq2U")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6446539222))

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001998669407'))

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6446539222").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


