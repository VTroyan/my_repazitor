"""
Этот модуль конвертирует градусы цельсия в фарингейты
"""
from prettytable import PrettyTable


def fahrenheit(celsius: int) -> str:
    """
    Конвертирует градусы цельсия в фарингейты
    :param celsius: значение в градусах по Цельсию
    :return: таблтца со значением в Фарингейтах и Цельсия

    '''
        +------------+---------+
        | Фаренгейты | Цельсия |
        +------------+---------+
        |     86     |   30.0  |
        +------------+---------+
    '''
    """
    fahrenheit_value = 5/9 * (celsius - 32)

    table = PrettyTable(["Фаренгейты", "Цельсия"])
    table.add_row([celsius, fahrenheit_value])

    return table.get_string()


print(fahrenheit(86))
