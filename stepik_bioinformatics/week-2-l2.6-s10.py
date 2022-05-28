#Напишите программу, на вход которой подаётся
#прямоугольная матрица в виде последовательности
#строк. После последней строки матрицы идёт строка,
#содержащая только строку "end"
#(без кавычек, см. Sample Input).

#Программа должна вывести матрицу того же размера,
#у которой каждый элемент в позиции i, j равен сумме
#элементов первой матрицы на позициях
#(i-1, j), (i+1, j), (i, j-1), (i, j+1).
#У крайних символов соседний элемент находится с
#противоположной стороны матрицы.

#В случае одной строки/столбца элемент сам себе
#является соседом по соответствующему направлению.


m = []                      # Создаём пустой список
buf = (input().split())     # Считываем пользовательский ввод
m.append(buf)               # Присоединяем введенную строку в конец массива
                            # как "элемент"
n = len(m[0])               # Запоминаем размерность введенной первой строки,
                            # чтобы последюущие строки не оказались "меньше"

while True:                 # Считываем ввод
    
    buf = input().split()   # Ввод :)

    if (buf[0] == "end"):   # Если это не end, то "работаем дальше"(с)
        break
    else:
        if(len(buf) == n):  # Если новая строка соответствует
                            # размеру первой строки, то добавляем
                            # её к нашей матрице
            m.append(buf)
        else:               # В противном случае, повторяем ввод
            print('Введите строку соответствующего размера:')
buf = 0                     # Очищаем буфер

# Цикл для вывода результата. Проход по элементам матрицы и
# вывод результата вычисления
for row in range(len(m)):
    for col in range(len(m[row])):
        buf = int(m[row - 1][col]) + int(m[row - len(m) + 1][col]) + \
              int(m[row][col-1]) + int(m[row][col - len(m[row]) + 1])
        # Вывод результата вычисления
        print(str(buf), end=' ')
        buf = 0
        # Перевод строки
        print()

#for row in range(len(m)):
#                                    # Перебираем row от 0 до "количества строк - 1"
#    for col in range(len(m[row])):  # Перебираем col от 0 до "количества колонок - 1"
#        print(m[row][col], end=' ') # Выводим элемент строки
#    print()                         # и переходим на новую строку

## Количество строк в массиве m
#print('Строки = ' + str(len(m)))
## Количество столбцов в строке 0
#print('Столбцы = ' + str(len(m[0])))
## Количество символов в элементе [0][2]
#print('Размер элемента = ' + str(len(m[0][2])))