#Напишите программу, которая принимает на вход список чисел
#в одной строке и выводит на экран в одну строку значения, которые #встречаются в нём более #одного раза.
#Для решения задачи может пригодиться метод sort списка.
#Выводимые числа не должны повторяться, порядок их вывода может быть #произвольным.

s = input().split()
s_sorted = sorted(s)
i = 0
while i < len(s):
	if(s_sorted.count(s_sorted[i])>1):
		print(s_sorted[i], end=' ')
		i += s_sorted.count(s_sorted[i])
	else:
		i += 1