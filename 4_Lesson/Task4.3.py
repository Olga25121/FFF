# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.

# number = int(input())
# for i in range(1, number+1):
#     for k in range(i):
#         print(i, end="")
#     print()

from random import randrange


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums


def uniq_el(list_nums: list):
    result = []
    my_dict = {}.fromkeys(list_nums, 0)

    for i in list_nums:
        my_dict[i] += 1

    for k in my_dict:
        if my_dict[k] == 1:
            result.append(k)

    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(uniq_el(all_list))
