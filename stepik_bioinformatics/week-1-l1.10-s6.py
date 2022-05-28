y = int(input())
if (not (y % 4) and y % 100) or (y % 400):
	print("Високосный")
else:
	print("Обычный")