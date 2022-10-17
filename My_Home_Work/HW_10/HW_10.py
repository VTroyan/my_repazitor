class MyException:
    print(
        "Для завершения нажмите "
        "Stop в качестве знака операции"
    )
    while True:
        operation = input("Введите значение операции: ")
        if operation == "stop":
            break
        if operation not in ("+", "-", "*", "/"):
            continue

        num_1 = int(input("Введите первое число: "))
        num_2 = int(input("Введите второе число: "))

        if operation == "+":
            print("Ответ: ", num_1 + num_2)
        elif operation == "-":
            print("Ответ: ", num_1 - num_2)
        elif operation == "*":
            print("Ответ: ", num_1 * num_2)
        elif operation == "/":
            try:
                print(num_1/num_2)
            except ZeroDivisionError as error:
                print("Делить на ноль нельзя")
