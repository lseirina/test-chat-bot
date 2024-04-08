""" библиотека environs загружает переменные из файла .env в окружение,
а затем может их оттуда читать"""
import os

# Чтение переменных окружения из файла .env.txt
with open('/app/.env.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split('=')
        os.environ[key] = value

# Теперь переменная окружения 'BOT_TOKEN' должна быть доступна
bot_token = os.getenv('BOT_TOKEN')

print(bot_token)














# import os
# from environs import Env

# env = Env()

# env.read_env()

# bot_token = env('BOT_TOKEN')

# print(bot_token)
