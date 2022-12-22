# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# in->6
# out->[2.0, 2.25, 2.37, 2.441, 2.488, 2.522] 14.071

n = int(input("Введите число: "))
def sequence(n):
    return[round((1 + 1 / n)**n, 3) for n in range (1, n + 1)]          
print(f"Последовательность: {sequence(n)}")
print(f"Сумма: {round(sum(sequence(n)), 3)}")

# Метод 2
# num = int(input())
# sum_nums = 0
# list_nums = []

# for n in range(1, n + 1):
#     result = round((1+1/n)**n, 3)
#     list_nums.append(result)
#     sum_nums += result
# print(list_nums)
# print(sum_nums)
