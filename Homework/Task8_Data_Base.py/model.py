import csv
from os import path

def csv_data_open():      # 1 - показать все
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=",")
        res = list(file_csv)
    return res

def add_info(list):  # 2- добавление информации
    with open("csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)

def del_info(index):  # удаление информации
    list_csv = csv_data_open()
    print(list_csv)
    del list_csv[index]
    with open("csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def update_info(index, tel):  # обновление информации
    list_csv = csv_data_open()
    list_csv[index[4]] = tel
    with open("csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

def import_into_csv():   # импорт из csv в txt формат
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file)
        res = list(file_csv)
    with open("txt_data.txt", 'w') as txt_file:
        for row in res:
            txt_file.writelines(row)
            txt_file.writelines('\n')

def error_enter():
    with open('log.csv', 'a', encoding='utf-8') as log_file:
        log_file.write(f'{"Enter error"}\n')



all_data = {}
last_id = 0
name_db = "employees_base.csv"

def read_all():
    global all_data, last_id

    # logging.info(f"Show all Show all entries. Database File - {name_db}")
    print(name_db)
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        # logging.warning(f"The database is not connected! Missing database file.")
        print("The database is not connected!")