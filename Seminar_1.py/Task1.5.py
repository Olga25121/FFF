# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве. 
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in   3, 6, 2, 1
# out  5.099
# AB = √AC2 + BC2. Формула Пифагора 
# AC = xb - xa;
# BC = yb - ya.

import math
xa = float(input("Введите координату x точки A: "))
ya = float(input("Введите координату y точки A: "))
xb = float(input("Введите координату x точки B: "))
yb = float(input("Введите координату x точки B: "))
distanceAB = math.sqrt((xb-xa)**2 + (yb-ya)**2)
print(round (distanceAB, 3))
