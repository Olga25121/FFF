# 3. Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in-1  out Negative value of the number of numbers! []

# in 10 out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

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
