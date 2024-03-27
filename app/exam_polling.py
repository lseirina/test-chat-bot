import requests
import time


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

offset = -2
updates: dict


def do_something() -> None:
    print('It was update.')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/upDates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something

    time.sleep(3)
    end_time = time.time()
    print(f'Time between requests: {end_time - start_time}')