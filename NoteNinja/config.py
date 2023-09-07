
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "22018080" # integer value, dont use ""
    API_HASH = "1cc4bac38c10d11ff9a68880cbdc1af3"
    TOKEN = "6309557731:AAFPD-48uzhXRqUFZYDku3FrxTg7RB55q90"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5003680905 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "the_support_chat"  # Your own group for support, do not add the @
    START_IMG = ""
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://USER_ID:PASSWORD@user.m23k7t3.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
