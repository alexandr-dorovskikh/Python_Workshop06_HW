# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

"""
a1 = int(input("a1 = "))
d = int(input("d = "))
count = int(input("Количество элементов = "))

progression = [a1 + (n - 1) * d for n in range(1, count + 1)]
print(progression)
"""

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

"""
from random import randint

lst = [randint(0, 100) for i in range(20)]
print("Исходный массив")
print(lst)

min_num = int(input("min = "))
max_num = int(input("max = "))

indexes = [i for i in range(len(lst)) if (lst[i] > min_num) and (lst[i] < max_num)]
print("Индексы")
print(indexes)

"""