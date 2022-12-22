# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

n = int(input("Введите значение N: "))
x = int (input("Первая позиция: "))
y = int (input("Вторая позиция: "))

list_num = []
for i in range(-n, n+1):
    list_num.append(i)
mult = list_num[x-1] * list_num[y-1]
print(f"Последовательность: {list_num}")
print(f"Произведение: {mult}")

# def range_numbers_n():  
#     print([*range(-n, n + 1)])
# range_numbers_n()
# for i in range(n):
#     if x == n:
#         mult = n[x-1]*n[y-1]
#     else:
#         print("?")
# print(f"Произведение элементов на указанных позициях: {n[x-1]}*{n[y-1]} =", mult)
# from random import randint
# numbers = []
# for i in range(10):
#     numbers.append(randint (-10,10))
# print(numbers)

# def get_numbers(numbers):
#     count =0 
#     for element in numbers:
#         count +=1
#     return count
# print('Number of elements: ', get_numbers(numbers))

# x = int(input('Enter  position of first element: '))
# y = int(input('Enter position of second element: '))

# for i in range(len(numbers)):
#     mult = numbers[x -1]*numbers[y - 1]
# print(f'Mult of elements: {numbers[x -1]} * {numbers[y -1]} =', mult)








