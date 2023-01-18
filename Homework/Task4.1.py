# 1. Вычислить число c заданной точностью d
# in Enter a real number: 9
#    Enter the required accuracy '0.0001': 0.000001
# out 9.000000

# in Enter a real number: 8.98785
#    Enter the required accuracy '0.0001': 0.001
# out 8.988

#1
from decimal import Decimal, getcontext

number = Decimal(input("Введите число: "))
accuracy= Decimal(input("Введите требуемую точность '0.0001': "))

def num_accuracy(n, a):

    print("Число с заданной точностью: ", n.quantize(a))

num_accuracy (number, accuracy)

#2
from decimal import Decimal


def accuracy(num, acc):
    number = Decimal(f"{num}")
    return number.quantize(Decimal(f"{acc}"))


print(accuracy(float(input("Enter a real number: ")), float(input("Enter the required accuracy 0.0001: "))))

#3
# --------------------------------------- 2 вариант

num = float(input('Enter a real number: '))

_, accu = input("Enter the required accuracy '0.0001': ").split(".")
print(f"{num:.{len(accu)}f}")