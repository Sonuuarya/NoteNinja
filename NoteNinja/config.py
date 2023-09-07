
class Config(object):
    LOGGER = True
   
    API_ID = "22018080" 
    API_HASH = "1cc4bac38c10d11ff9a68880cbdc1af3"
    TOKEN = "6309557731:AAFPD-48uzhXRqUFZYDku3FrxTg7RB55q90"  
    OWNER_ID = 5003680905
    
    SUPPORT_CHAT = "NoteNinjaSupport" 
    START_IMG = ""
    EVENT_LOGS = ()  
    MONGO_DB_URI= "mongodb+srv://USER_ID:PASSWORD@user.m23k7t3.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://sjjrieqz:5z19jX5hQE45xaN7aViiRnQ0xFVEyMZf@berry.db.elephantsql.com/sjjrieqz"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "GVUHVUJYKI8C693V"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "42RTE6OVQJK2"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="6969392047:FheF6ep48anTeyep" # get it from @FallenChat_Bot using /token
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
