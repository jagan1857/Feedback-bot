import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 13115322))

    API_HASH = str(os.environ.get("API_HASH", "f28fbd1367ddda2e6f863c3129323743"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "5672508866:AAFPM9AfazI58I8loqdQ9fOu4SPtc6DXGXk"))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1459910748))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1459910748").split())

    START = str(os.environ.get("START_TEXT", "Hello 👋 I am assistant for my ower. You can give feedback and als you can get help to anything from my owner 😊"))

    HELP = str(os.environ.get("HELP_TEXT", "Ooo you Need help. Ok ask me anything "))

    DONATE = str(os.environ.get("DONATE_TEXT", "Iam running all my services free of so, if possible you can donate any amount To me."))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "https://t.me/+cTsBLwDFiE44NzY1"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/My_Test_Botz"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/+cTsBLwDFiE44NzY1"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://Jagan:753753753@cluster0.zisdn.mongodb.net/?retryWrites=true&w=majority"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedback"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001712123362"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))

