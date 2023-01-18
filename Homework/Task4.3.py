# 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in-1  out Negative value of the number of numbers! []

# in 10 out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

#1
from random import randint

num = int(input("Введите длину списка: "))
if num < 1:
    print("Вы ввели отрицательное значение количества чисел!")

num_list = []
for i in range(num):   
    num_list.append(randint (0, 9))  
print(num_list)

temp = {}
for i in num_list:
    if i in temp:
        temp[i] = False
    else:
        temp[i] = True

output = [i for i in temp if temp[i]]

print(f"Cписок неповторяющихся элементов исходной последовательности:\n{output}")

#2

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

#3
from collections import Counter

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = Counter(lst)

single = [x for x, n in counter.items() if n == 1]
print(single)
