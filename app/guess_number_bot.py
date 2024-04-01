from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

import random


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

ATTEMPTS = 5

users = {}


def get_random_number() -> int:
    return random.randint(1, 100)


@dp.message(CommandStart())  # filter for '/start' command.
async def process_start_command(message: Message):
    """Check if user  has played already, if no, create a new dictionary."""
    # print(message.model_dump_json(indent=4, exclude_none=True)) using for getting inf about mesage.
    await message.answer(
        'Hello, let`s play in "guess number" game,\n'
        'To find the rules, send "/help"'
    )
    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }


@dp.message(Command(commands='help'))  # filter for '/help' command.
async def process_help_command(message: Message):
    """Show the rules."""
    await message.answer(
        'I will guess a number and you have 5 attempts to guess it.\n'
        'If you want to leave the game, send "/cancel" command.\n'
        'If you want to look at the statistic - send "/stat" command.'
    )


@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    """Show the statistic."""
    await message.answer(
        f"total_games: {users[message.from_user.id]['total_games']}\n"
        f"wins: {users[message.from_user.id]['wins']}"
    )


@dp.message(Command(commands='cancel'))
async def process_cancel_command(message: Message):
    """Cancel the game."""
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        users[message.from_user.id]['total_games'] += 1
        await message.answer("You left the game, if you want to start - just write.")
    else:
        await message.answer("We are not playing yet. Let`s start!")


@dp.message(F.text.lower().in_(['ok', 'yes', 'let`s play', 'play', 'I want']))
async def process_positive_answer(message: Message):
    if not users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['attempts'] = ATTEMPTS
        users[message.from_user.id]['secret_number'] = get_random_number()
        await message.answer('I guessed a number from 1 to 100. Try to guess it.')
    else:
        await message.answer('We are playing right now. Give me a number from 1 to 100.')


@dp.message(F.text.lower().in_(['no', 'i don`t want', 'nope']))
async def process_negative_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('We are playing right now. Give me a number from 1 to 100.')
    else:
        await message.answer('OK, maybe next time.')


@dp.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def process_numbers_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
            await message.answer('Huray, you guessed!!!')
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is smaller.')
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            users[message.from_user.id]['attempts'] -= 1
            await message.answer('My number is bigger.')
        else:
            await message.answer('Give me a number from 1 to 100.')

        if users[message.from_user.id]['attempts'] == 0:
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            await message.answer(
                "Sorry, but your five attempts is over.\n"
                f"My number was {users[message.from_user.id]['secret_number']}.\n"
                "Let`s play again?"
                )
    else:
        await message.Message('We have not played yet. Would you like to play?')


@dp.message()
async def process_any_other_answers(message: Message):
    """Handle other answers except the described ones."""
    if users[message.from_user.id]['in_game']:
        await message.answer('We are playing right now. Give me a number from 1 to 100.')
    else:
        await message.answer('I am just a bot. Let`s better play guessing game.')


if __name__ == "__main__":
    dp.run_polling(bot)
