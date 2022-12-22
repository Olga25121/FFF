# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# 6782 -> 23
# 0.67 -> 13
# 198.45 -> 27

float_num = input("Введите вещественное число: ")
sum = 0
for i in float_num:
    if i != ".":
        sum = sum + int(i)    
print(sum)

#Запрещенный метод
# print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))

# Метод "2"
# num = input()
# sum_digits = 0

# power = len(num)-2
# num = float(num)
# num *= int(10**power)

# while num:
#     sum_digits += int(num%10)
#     num //= 10
# print(int(sum_digits))

# 0.00000000000001
