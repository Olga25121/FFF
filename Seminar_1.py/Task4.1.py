# 1. Вычислить число c заданной точностью d
# in Enter a real number: 9
#    Enter the required accuracy '0.0001': 0.000001
# out 9.000000

# in Enter a real number: 8.98785
#    Enter the required accuracy '0.0001': 0.001
# out 8.988

from decimal import getcontext


# getcontext().clear_flags()
# n = int(input("Введите число: "))

# d= Decimal(input("Введите требуемую точность: "))
# getcontext(). = d

# print(f"Число{n}с заданной точностью: {d}")
getcontext().clear_flags()
d = int(input("Введите желаемую точность: "))
getcontext().prec = d
r = Decimal(input("Введите вещественное число: "))

print(f"Число {r:.{d}} с точностью {d} знаков")
