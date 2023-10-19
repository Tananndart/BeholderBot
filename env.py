from os import getenv

BOT_TOKEN = str(getenv("BOT_TOKEN"))
BOT_DATA_PATH = str(getenv("BOT_DATA_PATH"))
BOT_CHAT_ID = str(getenv("BOT_CHAT_ID"))
BOT_REMINDER_DAY_TIME = str(getenv("BOT_REMINDER_TIME"))
LOG_LEVEL = int(getenv("LOG_LEVEL"))

'''
log levels:
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
'''