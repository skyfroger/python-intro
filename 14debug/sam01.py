import friendly
friendly.install(lang="ru")

"""
Выведите на экран чётные числа от 1 до n.
Число n вводится с клавиатуры.
"""

n = int(input("Введите число n )

print("Чётные числа от 1 до", n)

for i in range(1, n + 1)
    if i % 2 == 0:
        print(i)
