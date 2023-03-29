# Задача 32: Определить индексы элементов списка, значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)
import random
list = [random.randint(0, 20) for i in range(20)]
print(list)
startpoint = int(input("Введите начало диапазона: "))
finishpoint = int(input("Введите конец диапазона: "))
print()
print("Индексы: ")
for i in range(len(list)):
    if startpoint < list[i] < finishpoint:
        print(i, end=", ")