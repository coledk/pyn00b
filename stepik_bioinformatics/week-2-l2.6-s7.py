#Напишите программу, которая считывает с консоли числа
#(по одному в строке) до тех пор, пока сумма введённых
#чисел не будет равна 0 и сразу после этого выводит
#сумму квадратов всех считанных чисел.
#Гарантируется, что в какой-то момент сумма введённых
#чисел окажется равной 0, после этого считывание
#продолжать не нужно.
#В примере мы считываем числа 1, -3, 5, -6, -10, 13;
#в этот момент замечаем, #то сумма этих чисел равна нулю
#и выводим сумму их квадратов, не обращая внимания на то,
#что остались ещё не прочитанные значения.

a = True
sm = 0
sm_sq = 0
while a:
    s = str(input())
    sm += int(s)
    sm_sq += int(s) ** 2 
    if(sm == 0):
        a = False
print(str(sm_sq))