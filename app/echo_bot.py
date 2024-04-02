from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))  # Filter to catch '/start'
async def process_start_command(message: Message):
    # React to the message '/start'.
    print(message.from_user.id)
    await message.answer('Hello')


@dp.message(Command(commands=['help']))  # Filter to catch '/help'
async def process_help_command(message: Message):
    # React to the message '/help'.
    await message.answer('How can I help you?')


@dp.message(F.voice)  # Filter to catch update with voice.
async def send_voice(message: Message):
    # Function catches the update voice type and send json file about it.
    print(message.model_dump_json(indent=4, exclude_none=True))  # for readable answer
    await message.reply('You send voice.')


@dp.message()
async def send_echo(message: Message):
    # Send the copy of your answer.
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="This update is not supported by method 'send_copy'")


if __name__ == "__main__":
    dp.run_polling(bot)
