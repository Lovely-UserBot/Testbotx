import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(os.environ.get("NO_OF_COLUMNS", 2))
        # emoji to be displayed  in help .legend
        NO_OF_COLUMNS = int(os.environ.get("NO_OF_COLUMNS", 2))
        # emoji to be displayed  in help .legend
        BL_CHAT = os.environ.get("BL_CHAT", "-1001344140905")
        G_BAN_LOGGER_GROUP = int(os.environ.get("G_BAN_LOGGER_GROUP", -1001169892177))
        FBAN_LOGGER_GROUP = os.environ.get("FBAN_LOGGER_GROUP", None)
        if FBAN_LOGGER_GROUP:
            FBAN_LOGGER_GROUP = int(FBAN_LOGGER_GROUP)

        EMOJI_IN_HELP1 = os.environ.get("EMOJI_IN_HELP1", "🚀 ")
        EMOJI_IN_HELP2 = os.environ.get("EMOJI_IN_HELP2", "⚡ ")
        ALIVE_EMOJI = os.environ.get("ALIVE_EMOJI", "⚜")
        # specify command handler that should be used for the plugins
        # this should be a valid "regex" pattern
        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
        HANDLER = os.environ.get("COMMAND_HAND_LER", r"\.")
        #custom animation to kang plugin
        CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
        # specify list of users allowed to use bot
        # WARNING: be careful who you grant access to your bot.
        # malicious users could do ".exec rm -rf /*"
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        # VeryStream only supports video formats
        VERY_STREAM_LOGIN = os.environ.get("VERY_STREAM_LOGIN", None)
        VERY_STREAM_KEY = os.environ.get("VERY_STREAM_KEY", None)
        GROUP_REG_SED_EX_BOT_S = os.environ.get("GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot")
        TEMP_DIR = os.environ.get("TEMP_DIR", None)
        CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
        watermark_path = os.environ.get("watermark_path", None)
        #Google Chrome Stuff
        CHROME_DRIVER = os.environ.get("CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver")
        GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
        # Google Drive ()
        G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
        G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
        if AUTH_TOKEN_DATA != None:
            os.makedirs(TMP_DOWNLOAD_DIRECTORY)
            t_file = open(TMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
            t_file.write(AUTH_TOKEN_DATA)
            t_file.close()

        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)
        GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
        #MongoDB
        MONGO_URI = os.environ.get("MONGO_URI", None)
        #alive
        ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
        PM_PIC = os.environ.get("PM_PIC", None)
        AWAKE_PIC = os.environ.get("AWAKE_PIC", None)
        HELP_PIC = os.environ.get("OP_PIC", None)
        ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
        PM_MSG = os.environ.get("PM_MSG", None)
        INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", "DISABLE")
        YOUR_GROUP = os.environ.get("YOUR_GROUP", "@Legend_Userbot")
        YOUR_CHANNEL = os.environ.get("YOUR_CHANNEL", "@Official_LegendBot.")
        BOT_PIC = os.environ.get("ALIVE_PIC", None)
        #auto bio
        BIO_MSG = os.environ.get("ALIVE_MSG", None)
        DEEP_AI = os.environ.get("DEEP_AI", "87d64af9-3126-41e8-8765-726bdd134ec8")
        #Lydia API
        LYDIA_API = os.environ.get("LYDIA_API",None)
        PLUGIN_CHANNEL = os.environ.get("PLUGIN_CHANNEL",None)
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/LEGEND-OS/LEGENDBOT"
        )
        APP_ID = os.environ.get("APP_ID", None)
        API_HASH = os.environ.get("API_HASH", None)
        LEGEND_STRING = os.environ.get("LEGEND_STRING", None)
        BOT_MODE = os.environ.get("BOT_MODE", "ON")
        BOTLOG = True
        EXTRA_PLUGIN = os.environ.get("EXTRA_PLUGIN", None)
        ASSISTANT = os.environ.get("ASSISTANT", None)
        ABUSE = os.environ.get("ABUSE", None)
        BOTLOG_CHATID = os.environ.get("LOGGER_ID", None)
        ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
        BOY_OR_GIRL = os.environ.get("BOY_OR_GIRL", "BOY")
        BOT_TRIGGER = os.environ.get("BOT_TRIGGER", "^/")
        BOTMODE_LOG = int(os.environ.get("BOTMODE_LOG", False))
        BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        FORCE_SUB = os.environ.get("FORCE_SUB", None)
        FORCE_CHANNEL_UN = os.environ.get("FORCE_CHANNEL_UN", None)
        LOGGER_ID = os.environ.get("LOGGER_ID", None)
        if LOGGER_ID:
            LOGGER_ID = int(LOGGER_ID)
        PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
        # can get from https://coffeehouse.intellivoid.net/
        RANDOM_STUFF_API_KEY = os.environ.get("RANDOM_STUFF_API_KEY", None)
        # github vars
        BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
        FORCE_CHANNEL_ID = int(os.environ.get("FORCE_CHANNEL_ID", False))
        EXTRA_LEGENDBOT = os.environ.get("EXTRA_LEGENDBOT", -1001221881562)
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
        GOOGLE_SEARCH_COUNT_LIMIT = int(os.environ.get("GOOGLE_SEARCH_COUNT_LIMIT", 9))
        # This is required for the speech to text module. Get your USERNAME from https://console.bluemix.net/docs/services/speech-to-text/getting-started.html
        IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
        IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
        # This is required for the hash to torrent file functionality to work.
        HASH_TO_TORRENT_API = os.environ.get("HASH_TO_TORRENT_API", "https://example.com/torrent/{}");
        LOGGER = True
        LOCATION = os.environ.get("LOCATION", None)
        OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
        OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
        SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
        # Send .get_id in any group to fill this value.
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\,")
        TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./userbot/DOWNLOADS/")
        TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "LEGENDBOT")
        TG_GLOBAL_ALBUM_LIMIT = int(os.environ.get("TG_GLOBAL_ALBUM_LIMIT", 9))
        # MIRROR ACE API KEY AND TOKEN
        MIRROR_ACE_API_KEY = os.environ.get("MIRROR_ACE_API_KEY", None)
        MIRROR_ACE_API_TOKEN = os.environ.get("MIRROR_ACE_API_KEY", None)
        # Telegram BOT Token from @Bot
        #spootifie
        SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME", None)
        SPOTIFY_PASS = os.environ.get("SPOTIFY_PASS", None)
        SPOTIFY_BIO_PREFIX = os.environ.get("SPOTIFY_BIO_PREFIX", None)
        #log
        DUAL_LOG = os.environ.get("DUAL_LOG", None)
        # DO NOT EDIT BELOW THIS LINE IF YOU DO NOT KNOW WHAT YOU ARE DOING
        # TG API limit. A message can have maximum 4096 characters!
        MAX_MESSAGE_SIZE_LIMIT = 100000
        # set blacklist_chats where you do not want userbot's features
        UB_BLACK_LIST_CHAT = set(int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split())
        # maximum number of messages for antiflood
        MAX_ANTI_FLOOD_MESSAGES = 5
        # warn mode for anti flood
        ANTI_FLOOD_WARN_MODE = ChatBannedRights(
            until_date=None,
            view_messages=None,
            send_messages=True
        )
        # chat ids or usernames, it is recommended to use chat ids,
        # providing usernames means an additional overhead for the user
        CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
        # Get your own API key from https://www.remove.bg/ or
        # feel free to use http://telegram.dog/Remove_BGBot
        REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
        # Set to True if you want to block users that are spamming your PMs.
        SLAP_USERNAME = os.environ.get("SLAP_USERNAME", None)
        GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
        GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
        NO_P_M_SPAM = bool(os.environ.get("NO_P_M_SPAM", True))
        # define "spam" in PMs
        NO_SONGS = bool(os.environ.get("NO_SONGS", False))
        MAX_FLOOD_IN_PM = int(os.environ.get("MAX_FLOOD_IN_PM", 7))
        #pm log
        PM_LOG_GRP_ID = os.environ.get("PM_LOG_GRP_ID", None)
        # set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
        NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", True))
        #heroku 
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
        # send .get_id in any channel to forward all your NEW PMs to this group
        PRIVATE_GROUP_BOT_API_ID = os.environ.get("PRIVATE_GROUP_BOT_API_ID", None)
        if PRIVATE_GROUP_BOT_API_ID:
            PRIVATE_GROUP_BOT_API_ID = int(PRIVATE_GROUP_BOT_API_ID)
        # send .get_id in your private channel to forward all your Private messages

        TAG_LOGGER = os.environ.get("TAG_LOGGER", None)
        if TAG_LOGGER: TAG_LOGGER = int(TAG_LOGGER)

        #Tag LOGGER

        PM_LOGGR_BOT_API_ID = os.environ.get("PM_LOGGR_BOT_API_ID", None)
        if PM_LOGGR_BOT_API_ID: PM_LOGGR_BOT_API_ID = int(PM_LOGGR_BOT_API_ID)
        # For Databases
        # can be None in which case plugins requiring
        # DataBase would not work
        DB_URI = os.environ.get("DATABASE_URL", None)
        # number of rows of buttons to be displayed in .legend command
        BUTTONS_IN_HELP = int(os.environ.get("NO_OF_BUTTONS", 7))
        NO_OF_BUTTONS = int(os.environ.get("NO_OF_BUTTONS", 7))
        
        #open load
        OPEN_LOAD_LOGIN = os.environ.get("OPEN_LOAD_LOGIN", None)
        OPEN_LOAD_KEY = os.environ.get("OPEN_LOAD_KEY", None)
        # number of colums of buttons to be displayed in .legend command
else:
    class Config(object):
        DB_URI = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True



if bool(ENV):
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    if CONSOLE_LOGGER_VERBOSE:
        basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=DEBUG,
        )
    else:
        basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=INFO)
    LOGS = getLogger("[Lêɠêɳ̃dẞø† 2.1]")

try:
    if Config.HEROKU_API_KEY is not None or Config.HEROKU_APP_NAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_API_KEY).apps()[
            Config.HEROKU_APP_NAME
        ]
    else:
        HEROKU_APP = None
except:
    HEROKU_APP = None


    # Check if the config was edited by using the already used variable.
    # Basically, its the 'virginity check' for the config file ;)
    CONFIG_CHECK = os.environ.get(
        "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

    if CONFIG_CHECK:
        LOGS.info(
            "Please remove the line mentioned in the first hashtag from the config.env file"
        )
        quit(1)

    # Logging channel/group configuration.
    BOTLOG_CHATID = os.environ.get("PLUGIN_CHANNEL", None)
    try:
        BOTLOG_CHATID = int(BOTLOG_CHATID)
    except:
        pass

    # Userbot logging feature switch.
    BOTLOG = sb(os.environ.get("BOTLOG", "True"))
    LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

    # Console verbose logging
    CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

    # SQL Database URI
    DB_URI = os.environ.get("DATABASE_URL", None)

    # OCR API key
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)
    GOOGLE_CHROME_BIN = os.environ.get("GOOGLE_CHROME_BIN", None)

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

    ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

    # FedBan Premium Module
    F_BAN_LOGGER_GROUP = os.environ.get("F_BAN_LOGGER_GROUP", None)

# Heroku Credentials for updater.
    HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "False"))
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

   
    # Youtube API key
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", None)

    # Default .alive name
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    AUTONAME = os.environ.get("AUTONAME", None)
    REDIRECTCHANNEL = os.environ.get("REDIRECTCHANNEL", None)

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY", "India"))

    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
   
    #custom sticker and animated
    CUSTOM_STICKER_PACK_NAME = os.environ.get("CUSTOM_STICKER_PACK_NAME", None)
    CUSTOM_ANIMATED_PACK_NAME = os.environ.get("CUSTOM_ANIMATED_PACK_NAME", None)

    # Custom Module
    PM_MSG = os.environ.get("PM_MSG", None)
    CUSTOM_AFK = os.environ.get("CUSTOM_AFK", None)

    # Upstream Repo
    UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/LEGEND-OS/LEGENDUSERBOT.git")

    # Last.fm Module
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    BIO_MSG = os.environ.get("BIO_MSG", None)

    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
    if not LASTFM_USERNAME == "None":
        lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                      api_secret=LASTFM_SECRET,
                                      username=LASTFM_USERNAME,
                                      password_hash=LASTFM_PASS)
    else:
        lastfm = None

    # Google Drive Module
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", None)
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
else:
    # Put your ppe vars here if you are using local hosting
    PLACEHOLDER = None
