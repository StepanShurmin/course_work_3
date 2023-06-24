'''Импортируем необходимые модули и функции.'''
import json
import datetime
from operator import itemgetter

from src.settings import FILE_PATH, DATE_FORMAT, ACCOUNT_MASK, CARD_MASK


def load_data():
    '''Открывает json-файл и преобразует в его список.'''
    with open(FILE_PATH, encoding='utf-8') as file:
        return json.load(file)


def get_last_executed_operations(data):
    '''Создаёт соответствующий условиям список, через генератор, и возвращает отсортированный по дате.'''
    executed_operations = [op for op in data if 'state' in op and op['state'] == 'EXECUTED']
    return sorted(executed_operations, key=itemgetter('date'), reverse=True)[:5]


def mask_card_number(card_number):
    '''Возвращает замаскированный номер карты.'''
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

    return f'{card_number[:len(name_card)]}{num_card_str[:7]}{CARD_MASK} {card_number[-4:]}'


def mask_account_number(account_number):
    '''Возвращает замаскированный номер счёта.'''
    return f'{ACCOUNT_MASK}{account_number[-4:]}'


def print_transactions(transactions_sorted):
    '''Выводит на экран список из 5 последних выполненных клиентом операций.'''
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
