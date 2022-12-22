# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

num_list = []
n = int(input("Введите число: "))
f=1
for i in range (1, n + 1):
    f=f*i
    num_list.append(f)
print(num_list)






# n = int(input('Введите число: '))
# f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
# list2 = list( f(i) for i in range(1, n +1))
# print(list2)

