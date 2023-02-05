from model import *
from exception import *
from controller import * 


def show_menu():
    print('------------------------------')
    print(f"Информационная система RusLab:\n{'-' * 30}")
    print('1 - Показать все записи')
    print('2 - Найти запись')
    print('3 - Добавить запись')
    print('4 - Редактировать запись')
    print('5 - Удалить запись')
    print('6 - Экспорт/Импорт')
    print('7 - Выход')
    return int(input("Выберите пункт меню: "))