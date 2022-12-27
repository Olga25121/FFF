# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# in 54  out [2, 3, 3, 3]
# in 9990  out  [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]

n = int(input("Введите натуральное число N: "))

prime_factors = []
for i in range(n-1, 1, -1):
    num_prime = 0
    if (n % i == 0):
        for j in range(i-1,1,-1):
            if(i % j == 0):
                num_prime = num_prime + 1
        if(num_prime == 0):
            prime_factors.append(i)
print(f"Простые множители числа: {prime_factors}")




