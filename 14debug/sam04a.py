import friendly
friendly.install(lang="ru")

"""
Дан список, который содержит пункты меню для кофе-машины.
Программа выводит пронумерованный список доступных вариантов,
а затем просит пользователя выбрать один из пунктов.

Если выбран номер, которого нет в списке, программа должна
вывести сообщение "Такого варианта у нас нет"
"""

coffee_items = ["эспрессо", "американо", "латте", "мокко", "каппучино"]

for i in range(len(coffee_items)):
    number = i + 1
    print(number, coffee_items[number])

user_choiсe = int(input("Какой кофе вы хотите заказать? "))

print("Вы заказали", coffee_items[user_choiсe])