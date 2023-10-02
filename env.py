from os import getenv

BOT_TOKEN = getenv("BOT_TOKEN")                         # уникальный токен доступа бота
BOT_DATA_PATH = getenv("BOT_DATA_PATH")                 # папка для хранения данных бота
BOT_CHAT_ID = getenv("BOT_CHAT_ID")                     # идентификатор чата с ботом
BOT_REMINDER_DAY_TIME = getenv("BOT_REMINDER_TIME")     # время вопроса бота о статусе дня, например "23:00"
