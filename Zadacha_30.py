# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_elem = int(input("Введите первый элемент прогрессии: "))
step = int(input("Введите шаг прогрессии: "))
numbers_elem = int(input("Введите количество элементов прогрессии: "))

progression = [i + first_elem for i in range(0, numbers_elem * step, step)]

print(progression)
