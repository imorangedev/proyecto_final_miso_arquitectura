from os import getenv

# External routes
DB_HOST = getenv('DB_HOST', None)
DB_USER = getenv('DB_USER', None)
DB_PWD = getenv('DB_PWD', None)
DB_NAME = getenv('DB_NAME', None)

DATABASE_URI = f'postgresql+pg8000://{getenv(DB_USER)}:{getenv(DB_PWD)}@{getenv(DB_HOST)}/{getenv(DB_NAME)}'