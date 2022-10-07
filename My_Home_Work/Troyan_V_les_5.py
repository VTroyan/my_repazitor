"""В данном модуле представлено 2 задания"""
# 1 - Декоратор.
"""В этой функции мы используем декоратор и 2 аргумента Имя, Фамилию"""
# def decorator(my_func):
#     def wraper(*args, **kwargs):
#         print("Начало декоратора")
#         my_func(*args, **kwargs)
#         print("Конец декоратора")
#
#     return wraper
# @decorator
# def say(name, surname):
#     print("Привет", name, surname)
#
# say("Петя", "Петров")

# 2 - Лямбда функция.
"""Пример с урока"""
# num1 = list(map(lambda x: x * x,[2,4,6,8]))
# print(num1)
"""Пример без map"""
# print((lambda a, b: a * b)(5, 5))