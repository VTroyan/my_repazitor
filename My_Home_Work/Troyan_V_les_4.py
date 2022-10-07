# (Упрощённый вариант)
# Задание 1 Генератор списка
# ------------------------------------
# list_a = [a*2 for a in range(10)]
# print(list_a)


Задание 2 Функция для генерации с анотациями
def my_func(name: str = None) -> tuple:
    num = input("Введите имя ")
    name = [name for a in range(10)]
    print(name)
my_func()



