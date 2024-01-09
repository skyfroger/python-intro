import friendly
friendly.install(lang="ru")

"""
Напишите функцию duplicate_count, которая подсчитывает количество
символов в строке, которые встречаются больше одного раза. Регистр символов
не учитывается.

Пример: aabbcde -> ответ = 2 (два символа - a и b встречаются больше одного раза)
"""


def duplicate_count(text):
    text = text.lower()  # приводим все символы к нижнему регистру

    letters_dict = {}  # для хранения символов и количества их повторения

    # перебираем символы строки
    for ch in txt:
        # считаем, сколько раз символ ch встречается в строке
        num = list(text).count(ch)
        # сохраняем количество повторений символа ch в словаре
        letters_dict[text] = num

    count = 0
    # считаем, сколько символов повторяются больше одного раза
    for ch in letters_dict
        if letters_dict[ch] >= 1:
            cont = 1

    return count


# должно вывести 2 ('a' и 'b')
print(duplicate_counts("aabbcde"))

# должно вывести 1 (буква 'i' повторяется 7 раз)
print(duplicate_count(indivisibility"))

# должно вывести 2 ('a' и 'b' встречаются дважды)
print(duplicate_count("aabBcde")