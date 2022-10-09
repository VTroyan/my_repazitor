# Задание 3*
print("Игра Угодай Число !")
import random
guesses_made = 0
name = input('Здравствуйте, как к вам можно обращаться ? ')
number = random.randint(1, 30)
print("Отлично, я загодал число от одного до до тридцати, "
      "сможешь угадать ?")
print("если вы готовы рискнуть - у вас 5 попыток")
while guesses_made < 5:
    guess = int(input("Введи число: "))
    guesses_made += 1
    if guess < number:
        print("Ваше число меньше загаданного")
    if guess > number:
        print("Ваше число больше загаданного")
    if guess == number:
        break
if guess == number:
    print("Ты угодал")
else:
    print("НЕ угодал")

