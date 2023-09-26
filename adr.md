# 30.08.23 Why was aiogram chosen?
- based on this [article](https://habr.com/ru/articles/543676/)
- Among bot developers, the best Python bot library is aiogram. It is asynchronous, uses decorators, and provides handy development tools.

# 30.08.23 Почему через пулинг, а не через вебхуки с сервервом Telegram работаем?
- вебхуки это оптимизация. Они нужны будут в случае повышенной нагрузки
- нагрузка планируется на одного пользователя, т.е. небольшая, потому смысла усложнять нет

# 26.09.2023 Почему для хранения выбран формат csv?
- ради скорости разработки и простоты
- специально закрываем его за абстрактным репозиторием, чтобы можно было легко поменять потом
