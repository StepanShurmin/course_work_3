from src.functions import mask_account_number, mask_card_number, get_last_executed_operations, load_data


def test_load_data():
    data = load_data()
    assert isinstance(data, list)


def test_mask_card_number():
    card_number = 'MasterCard 1796816785869527'
    expected_result = 'MasterCard 1796 81** **** 9527'
    assert mask_card_number(card_number) == expected_result

    card_number = 'Maestro 9171987821259925'
    expected_result = 'Maestro 9171 98** **** 9925'
    assert mask_card_number(card_number) == expected_result

    card_number = 'МИР 2052809263194182'
    expected_result = 'МИР 2052 80** **** 4182'
    assert mask_card_number(card_number) == expected_result

    card_number = 'Счет 97848259954268659635'
    expected_result = 'Счет 9784 82** **** 9635'
    assert mask_card_number(card_number) == expected_result


def test_mask_account_number():
    account_number = 'Счет 14073196441261107791'
    expected_result = '**7791'
    assert mask_account_number(account_number) == expected_result


def test_get_last_executed_operations():
    data = [
        {'state': 'EXECUTED', 'date': '01.05.2022'},
        {'state': 'EXECUTED', 'date': '03.05.2022'},
        {'state': 'CANCELED', 'date': '07.05.2023'},
        {'state': 'EXECUTED', 'date': '05.05.2023'},

    ]
    expected_result = [
        {'state': 'EXECUTED', 'date': '05.05.2023'},
        {'state': 'EXECUTED', 'date': '03.05.2022'},
        {'state': 'EXECUTED', 'date': '01.05.2022'},
    ]
    assert get_last_executed_operations(data) == expected_result

    data = []
    expected_result = []
    assert get_last_executed_operations(data) == expected_result


data = [{'state': 'EXECUTED', 'date': '22.06.2023'}, {'state': 'EXECUTED', 'date': '21.06.2023'},
        {'state': 'EXECUTED', 'date': '20.06.2023'}, {'state': 'EXECUTED', 'date': '19.06.2023'},
        {'state': 'EXECUTED', 'date': '18.06.2023'}, {'state': 'CANCELED', 'date': '17.06.2023'},
        {'state': 'CANCELED', 'date': '16.06.2023'}, {'state': 'EXECUTED', 'date': '15.06.2023'},
        {'state': 'EXECUTED', 'date': '14.06.2023'}, {'state': 'CANCELED', 'date': '13.06.2023'}]
assert get_last_executed_operations(data) == data[:5]
