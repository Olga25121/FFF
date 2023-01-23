# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

#1
from random import randrange

def list_rand_nums(count: int):
    if count < 0:
        print("Вы ввели отрицательное значение количества чисел!")
        return []

    list_nums = []
    for i in range(count):
        list_nums.append(randrange(count))

    return list_nums

def list_bigger_elem(list_nums: list):
    
    result = [list_nums[i] for i in range(1, len(list_nums)) if list_nums[i] > list_nums[i-1]] 
    return result

all_list = list_rand_nums(int(input("Введите длину списка: ")))
print(all_list)
print(list_bigger_elem(all_list))

#2
from random import sample


def more_then(num):
    my_list = sample(range(num * 3), num)
    print(my_list)
    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]


print(more_then(int(input())))

#  ------------------------------------------- вариант решения ---------------------------------------------------------

from random import randint


def more_then(num):
    original_list = [randint(0, 1000) for _ in range(num)]
    print(original_list)
    return [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]


print(more_then(int(input())))