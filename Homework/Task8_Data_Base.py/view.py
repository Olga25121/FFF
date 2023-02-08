from model import *
from exception import *
from controller import * 


def show_menu():
    print('------------------------------')
    print(f"Информационная система RusLab:\n{'-' * 30}")
    print('1 - Показать все записи')
    print('2 - Найти запись')
    print('3 - Добавить запись')
    print('4 - Редактировать телефон')
    print('5 - Редактировать должность')
    print('6 - Редактировать фамилию')
    print('7 - Удалить запись')
    print('8 - Экспорт/Импорт')
    print('9 - Выход')
    return int(input("Выберите пункт меню: "))
