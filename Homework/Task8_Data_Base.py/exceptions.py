from model import error_enter, search


def user_choice():
    choice1 = input('Please enter you choice: ')
    try:
        choice1 = int(choice1)
        if (choice1 > 7) and (choice1 < 0):
            print('Error')
            return user_choice()
        else:
            return choice1
    except ValueError:
        print('Error')
        error_enter()
        return user_choice()


def data_search():
    try:
        my_search = input('Enter a position to search for employees: ')
        search(my_search)

    except ValueError:
        print('Error')
        error_enter()
    return my_search
# def find_entry(data_find, all_info):
#     logging.info(f"Search for an entry: {data_find}")
#     candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
#     if candidates:
#         logging.info(f"Search result: {candidates}")
#         print(*candidates, sep="\n", end="\n\n")
#         return [n[0] for n in candidates]
#     else:
#         logging.warning(f"No data found: {data_find}")
#         print("Name or phone number not found.\n")
#         return 0