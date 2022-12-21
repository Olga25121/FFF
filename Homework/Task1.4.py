# 4. Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (quarter и y).

# *Пример:*
# - 1 -> quarter > 0, y > 0
# - 8 -> нет такой четверти

quarter = int (input("Введите номер четверти плоскости от 1 до 4: "))
if quarter == 1:
    print("x > 0 and y > 0") 
elif quarter == 2:
    print("x < 0 and y > 0")
elif quarter == 3:
    print("x < 0 and y < 0") 
elif quarter == 4:
    print("x > 0 and y < 0")
else:
    print("Номер четверти плоскости введен некорректно!")

# Без преобразования сразу работать со строковыми
# quarter = input()
# match quarter:
#     case "1":
#         print("x > 0, y > 0")
#     case "2":
#         print("x < 0, y > 0")
#     case "3":
#         print("x < 0, y < 0")
#     case "4":
#         print("x > 0, y < 0")    
#     case _:
#         print("error")    

    
    

