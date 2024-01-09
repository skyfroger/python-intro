import friendly
friendly.install(lang="ru")

"""
Найти сумму цифр числа и записать её в следующем формате:
цифра + цифра + цифра + ... = сумма цифр

Число вводится с клавиатуры.

Пример:
Введите число: 256
2 + 5 + 6 = 13
"""

num = int(input("Введите число: "))

# находим сумму цифр числа num
sum = 0
for dig in str(num):
    sum += int(dig)

# --- исправьте ошибку в коде ниже ---

result = " + ".join(list(num)) + " = " + sum

# --- исправьте ошибку в коде выше ---
print(result)