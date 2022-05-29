def update_dictionary(d, key, value):

    # Проверка есть ли переданный ключ в словаре
    if key in d:
        #Ключ найден, добавляем значение к ключу
        d[key].append(value)
        return

    # "Работаем дальше" (с)
    else:
        # Меняем ключ согласно условию задачи
        key *= 2
        # Проверяем есть ли новый ключ
        if key in d: 
            # Ключ найден, добавляем значение к ключу
            d[key].append(value)
            return
 
        else:      
            # Добавляем новый ключ и его значение [списком]
            d[key] = [value]
            return

d = {} # Создаем пустой словарь
update_dictionary(d, 1, -1)
print("Dictionary is ", d, end="\n\n")

update_dictionary(d, 2, -2)
print("Dictionary is ", d, end="\n\n")

update_dictionary(d, 3, -3)
print("Dictionary is ", d, end="\n\n")
exit()

