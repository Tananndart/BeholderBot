
def get_text_without_command(message_text: str):
    """
    Возвращает текст сообщения без введенной команды.
    /day good -> good
    :param message_text: текст сообщения.
    :return: Текст сообщения без указанной команды.
    """
    if message_text.startswith("/"):
        prefix_length = len(message_text.split()[0])
        return message_text[prefix_length:].strip()

    return message_text
