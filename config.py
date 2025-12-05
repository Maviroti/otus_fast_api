from os import getenv

db_url = "postgresql+psycopg://admin:12345678@127.0.0.1:5432/tasker"

sqla_max_overflow = 0
sqla_pool_size = 50

# всегда False
db_echo = False


# только по переменной окружения можем включить
if getenv("DB_ECHO") == "1":
    db_echo = True
