from aiogram import Bot, Dispatcher
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def my_start_filter(message: Message) -> bool:
    """"Filter for /start command."""
    print(message.model_dump_json(indent=4, exclude_none=True))
    return message.text == '/start'



# a = lambda s: sum(1 for c in s.lower() if c == 'я') >= 23

# count = 0
# for c in s:
#     if c.lower() == 'я':
#         count += 1

# if count >= 23:
#     return True
# return False

# print(a('яя яяяяяяяяяяяя тоже!'))


def custom_filter(some_list) -> bool:
    count = 0
    for i in some_list:
        if isinstance(i, int) and i % 7 == 0:
            count += i
    if count < 83:
        return True
    return False


print(custom_filter([7, 14, 28, 32, 32, 56]))

@dp.message(lambda mesg: mesg.text == '/start')
async def process_start_command(message: Message):
    await message.answer(text='It is a start-command.')


if __name__ == "__main__":
    dp.run_polling(bot)
