import friendly
friendly.install(lang="ru")

"""
Дан список строк. Выведите на экран те строки, длина которых больше 4 но меньше 8.
Вместе со строками выведите её индекс в списке.
"""

words = ["class", "if", "def", "continue", "return"]

words_len = len(words)  # количество слов в списке

# перебираем список слов
for i in range(1, words_len):
    w = words[i]
    if len(w) > 4 or len(w) < 8:
        print(i, w)

# Ожидаемый ответ:
# 1 class
# 5 return