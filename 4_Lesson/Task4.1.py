# 1. Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# in -> 11 23 90 -8 12 7 45 -44  out  -44 90
# in 1, 6. 8: 9! out -4 9
# in 1 y 6 г 8 out  "The data is incorrect"

def user_input(user_str):
    new_str = user_str.split()
    lst = []

    for i in range(len(new_str)):
        new_str[i] = new_str[i].strip(".,;!")
        if new_str[i].replace("-", "", 1).isdigit():
            lst.append(new_str[i])
            
    return lst

def user_output(lst):
    if lst:
        return max(lst, key=int), min(lst, key=int)
    return"Something strange"

print(user_output(user_input(input("..."))))