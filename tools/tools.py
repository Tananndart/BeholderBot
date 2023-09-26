from aiogram.types import Message
import re


def get_message_text(message: Message):
    text = message.text
    if text.startswith("/"):
        prefix_length = len(text.split()[0])
        return text[prefix_length:].strip()

    return text

