'''Импортируем модуль для построения абсолютного пути до файла.'''
import os

'''Прописываем путь до файла.'''
PATH = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = os.path.join(PATH, "../operations.json")

'''Создаем константы для изменения формата даты и для маскирования счёта и номера карты.'''
DATE_FORMAT = '%d.%m.%Y'
CARD_MASK = '** ****'
ACCOUNT_MASK = '**'

