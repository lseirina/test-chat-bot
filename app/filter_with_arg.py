"""Bot using filter with arguments."""
from aiogram import Bot, Dispatcher, F
from aiogram.filters import BaseFilter
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        for word in message.text.split():
            norm_word = word.replace(',', '').replace('.', '').strip()
            if norm_word.isdigit():
                numbers.append(int(norm_word))
        if numbers:
            return {'numbers': numbers}
        return False


@dp.message(F.text.lower().startswith('find numbers'), NumbersInMessage())
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(text=f'Found: {", ".join(str(num) for num in numbers)}')


@dp.message(F.text.lower().startswith('find numbers'))
async def process_if_not_numbers(message: Message):
    await message.answer(text='I did not find anything')


if __name__ == "__main__":
    dp.run_polling(bot)
