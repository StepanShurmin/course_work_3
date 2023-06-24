import json
import datetime
from operator import itemgetter

from src.settings import FILE_PATH, DATE_FORMAT


def load_data():
    with open(FILE_PATH, encoding='utf-8') as file:
        return json.load(file)


def get_last_executed_operations(data):
    executed_operations = [op for op in data if 'state' in op and op['state'] == 'EXECUTED']
    return sorted(executed_operations, key=itemgetter('date'), reverse=True)[:5]


def mask_card_number(card_number):
    CARD_MASK = '** ****'
    num_card = []
    name_card = []
    for i in card_number:
        if str(i).isalpha() or i == ' ':
            name_card.append(i)
        else:
            num_card.append(i)


    num_len = len(num_card)


    num_card_parts = [''.join(num_card[i:i + 4]) for i in range(0, num_len, 4)]
    num_card_str = ' '.join(num_card_parts)


    return f'{card_number[:len(name_card)]} {num_card_str[:7]} {CARD_MASK} {card_number[-4:]}'


def mask_account_number(account_number):
    ACCOUNT_MASK = '**'
    return f'{ACCOUNT_MASK}{account_number[-4:]}'


def print_transactions(transactions_sorted):
    for op in transactions_sorted:
        date = datetime.datetime.fromisoformat(op['date']).strftime(DATE_FORMAT)
        description = op['description']
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        if 'from' in op:
            from_account = mask_card_number(op['from'])
            to_account = mask_account_number(op['to'])
            print(f'\n{date} {description} \n{from_account} -> Счет {to_account} \n{amount} {currency}\n')
        else:
            to_account = mask_account_number(op['to'])
            print(f'\n{date} {description} -> Счет {to_account} \n{amount} {currency}\n')

