# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in -> 4   out ->[2, 5, 8, 10]  [20, 40]
# in -> 5   out ->[2, 2, 4, 8, 8]  [16, 16, 4]

# from random import randint

# num = int(input("Введите длину списка: "))
# num_list = []

#     num_list.append(randint (1, 10))
#     if len(num_list) % 2 != 0:
#         pair_list = len(num_list)//2 + 1
#     else:
#         len(num_list)//2
#     pair_list = [num_list[i]*num_list[len(num_list)-i -1]]
#     print(pair_list)
# print(num_list)

import random

n = int(input("Введите длину списка: "))
num_list = [random.randint(1, 10) for i in range(n)]


def multiple_nums(element):
    pair_list = []
    for i in range((len(element) + 1) // 2):
        pair_list.append(element[i] * element[len(element) - 1 - i])
    return pair_list

print(num_list, end=" =>")
print(multiple_nums(num_list))

# [6, 6, 7, 8] =>[48, 42]