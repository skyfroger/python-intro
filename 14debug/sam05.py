import friendly
friendly.install(lang="ru")

"""
Сформируйте список состоящий из n случайных чисел в отрезке от 0 до 10
(n вводится с клавиатуры), и выведите его на экран.

Затем найдите сумму нечётных чисел в списке.
"""

from random import randint

n = int(input("Введите n "))

lst = []  # список для хранения чисел

# заполняем список n случайными числами
for i in range(n):
    num = randint(0, 10)
    lst.append(num)

print("Список случайных чисел")
# выводим список со случайными числами
for i in range(50):
    print(lst[i])

sum = 0
for num in num_lst:
    if num % 2 != 0:
        sum += num

print("Сумма нечётных чисел:", summa)