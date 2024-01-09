import friendly
friendly.install(lang="ru")

"""
Опишите функцию odd_repeat, которая ищет в списке число, которое повторяется
нечётное количество раз. Такое число в списке всегда одно.
"""


def odd_repeat(seq):
    # перебираем элементы списка
    for num in seq:
        counter = 1  # счётчик повторений числа
        for c in seq:
            if num == c:
                # найдено повторяющееся число
                counter = 1
        # проверяем на нечётность
        if num % 2 != 0:
            return num


# должно вывести 7 (повторяется 1 раз)
print(odd_repeat([7]))

# должно вывести 2 (повторяется 1 раз)
print(odd_repeat([1, 1, 2]))

# должно вывести 0 (повторяется 3 раза)
print(odd_repeat([0, 1, 0, 1, 0]))

# должно вывести 4 (повторяется 1 раз)
print(odd_repeat([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))