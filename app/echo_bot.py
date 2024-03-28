from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Hello')


async def process_help_command(message: Message):
    await message.answer('How can I help you?')


async def send_photo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


async def send_echo(message: Message):
    await message.reply(text=message.text)


dp.message.register(process_start_command, Command(commands=['start']))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo, F.photo)
dp.message.register(send_echo)


if __name__ == "__main__":
    dp.run_polling(bot)
