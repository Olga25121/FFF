# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in -> 5  out ->[5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in -> 3  out ->[9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform

def float_num_list(count):
    list_nums = []
    if count <= 0:
        print("Ошибка! Вы ввели отрицательное число")
        return [-1]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def diff_nums(list_nums):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
              num_min = num

    result = round(num_max - num_min, 2)
    print(f"Минимальное: {num_min}, Максимальное: {num_max}. Разница: {result}")
    return result
    
all_list = float_num_list(int(input("Введите длину списка: ")))
print(all_list)
print(diff_nums(all_list))