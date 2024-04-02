"""My own filter which is similar to the built-in filter in aiogram."""
# id = 2071954957
from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

admin_ids = [2071954957

             ]
class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message):
        return message.from_user.id in self.admin_ids

@dp.message(IsAdmin(admin_ids))
async def answer_admin_update(message: Message):
    await message.answer(text='You are admin.')


@dp.message()
async def answer_not_admin_update(message: Message):
    await message.answer(text='You are not admin.')


if __name__ == "__main__":
    dp.run_polling(bot)
