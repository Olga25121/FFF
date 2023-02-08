import csv
from optparse import Values
from exception import *
from logger import logging

input_id_employee = 0
user_choice_second = 0

def list_menu():
    global input_id_employee
    global user_choice_second 



def import_dictionary():
    with open("python.csv", mode="r", encoding='utf-8') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict

def show_all():   # 1 - Показать все записи
    with open("python.csv", "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        for line in reader:
            print(line)


def find_employee(k):       # 2 - Найти запись
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                print(i)



def add_employee():         # 3 - Добавить запись
    print('Введите данные нового сотрудника через ENTER: ')
    id = input('id: ')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    position = input('Должность: ')
    salary = input('Зарплата: ')
    with open('python.csv', mode="a", encoding='utf-8') as python:
        new_employee = f'\n{id},{name},{surname},{position},{salary}\n'
        python.write(new_employee)
        print('Новая запись добавлена')


def change_data(): # 4 - Редактировать запись
    k = input('Введите старые данные: ')
    new_val = input('Введите новые данные: ')
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                value == new_val
    with open('python.csv', mode="w", encoding='utf-8', newline='') as python:
        fc = csv.DictWriter(python, fieldnames=array[0].keys())
        fc.writeheader()
        fc.writerows(array)    

def update_data(index, pos):  # 4 - обновление информации
    list_csv = show_all()
    list_csv[index[0]] = pos
    with open("python.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

def change_data():  # по номеру id меняем данные о сотруднике и перезаписываем строку
    array = import_dictionary()
    with open("python.csv") as f:
        data = [i for i in array]
        for line in data:
            if(int(line[0])==selectedId): 
                line[user_choice_second] = input_update



def delete_employee(k):    # 5 - Удалить запись
    array = import_dictionary()
    for i in array:
        for value in i.values():
            if value == k:
                array.remove(i)
    with open('python.csv', mode="w", encoding='utf-8', newline='') as python:
        fc = csv.DictWriter(python, fieldnames=array[0].keys())
        fc.writeheader()
        fc.writerows(array)
        print("Запись удалена.")



def export_import():       # 6 - Экспорт csv в txt
    logging.info(f"Start menu export/import.")
    choise = input('1. - Export\n'
                   '2. - Import\n')
    match choise:
        case "1":
            logging.info('Start export.')
            with open('new.txt', "w", encoding='utf-8') as my_output_file:
                with open('python.csv', "r", encoding='utf-8') as my_input_file:
                    [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
                    my_output_file.close()
                    print('Выполнен экспорт csv файла в txt формат')
                return my_output_file


        case "2":           # -  Импорт csv в txt
            logging.info('Start import.')
            with open("new.txt", "r" , encoding='utf-8') as f:
                reader = csv.reader(f, delimiter=",")
                for line in reader:
                    print('Выполнен импорт txt файла в csv формат')
                    return line
        case _:
                logging.warning("Main menu, wrong item selected.")
                print("The menu item is not recognized. Try again!")


def finish_work():       # 7 - Выход
    print("Вы вышли из главного меню.")







def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))

def count(): # считаю ID: кол-во строк в файле + 1
    count = 0
    for line in open("python.csv"):
        count+= 1
    return count

def get_next_id():
    global id
    id = count() + 1
    return id

def setSelected(entered_id):
    global selectedId
    selectedId = entered_id

def second_select(choice_second):
    global user_choice_second
    user_choice_second = choice_second

def update_data(data):
    global input_update
    input_update = data