import logging
import csv

def find_entry(data_find, all_info):
    logging.info(f"Search for an entry: {data_find}")
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        logging.info(f"Search result: {candidates}")
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Name or phone number not found.\n")
        return 0

def matching_rec(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def check_new_data(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "name surname description":
            if answer.isalpha():
                break
        if num == "phone":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer

def save_csv(file_name):
    logging.info(f"Export in csv format: {file_name}.csv")

    with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('python.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fieldnames = ["id", "name", "surname", "phone", "email", "position", "salary"]
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
        print(f"{file_name}.csv file saved\n")