# Напишите программу, которая подключает
# модуль math и, используя значение числа \pi
# из этого модуля, находит для переданного ей
# на стандартный ввод радиуса круга периметр
# этого круга и выводит его на стандартный вывод.

import math
r = float(input())
print(2 * math.pi * r)

# Или...
#from math import tau
#print(float(input()) * tau)

# Или...
#print(__import__('math').pi * 2 * float(input()))
