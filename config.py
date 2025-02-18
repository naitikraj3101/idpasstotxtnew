from os import getenv


API_ID = int(getenv("API_ID", "24473318"))
API_HASH = getenv("API_HASH", "e7dd0576c5ac0ff8f90971d6bb04c8f5")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "5840594311"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5840594311").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://tusartxt7570:K1AVnnJlDceZBiRY>@cluster0.78fhl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002481146756"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", ""))


