class MyException(Exception):
    def __init__(self, msg="Моя ошибка по умолчанию"):
        self.msg = msg

    def __str__(self): return self.msg


print(
    "Для завершения нажмите "
    "Stop в качестве знака операции"
)


while True:
    operation = input("Введите значение операции: ")
    if operation == "stop":
        break
    elif operation not in ("+", "-", "*", "/"):
        continue
    # Цикл для ввода переменных, если возникает ошибка то цикл повторяеется
    while True:
        try:
            num_1 = int(input("Введите первое число: "))

        except ValueError:
            continue

        try:
            num_2 = int(input("Введите второе число: "))

        except ValueError:
            continue

        if operation == "+":
            print("Ответ: ", num_1 + num_2)
        elif operation == "-":
            print("Ответ: ", num_1 - num_2)
        elif operation == "*":
            print("Ответ: ", num_1 * num_2)
        elif operation == "/":
            try:
                print(num_1 / num_2)
            except ZeroDivisionError:
                raise MyException()
                # print("Делить на ноль нельзя")

        break
