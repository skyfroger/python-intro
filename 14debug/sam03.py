import friendly
friendly.install(lang="ru")

"""
Вычислить среднее арифметическое двух вещественных чисел,
которые вводятся с клавиатуры.
"""

n1 = input("Первое число: ")
n2 = input("Второе число: ")

avg = (n1 + n2) / 2

print("Ответ:", avg)