#! /usr/bin/env python
# -*- coding: utf-8 -*
import random                       # Ввести модуль случайных чисел
print('start game')
print('you just have three chance to attempt')
randnum=random.randint(1,20)         # Генерация случайного числа от 1 до 20
n=0
while n<3:
    temp=input('please input a number between 1 to 20:')
    num=int(temp)
    if num>20:
        print('error input,input beyond scope')
    else:
        if num<1:#! /usr/bin/env python
# -*- coding: utf-8 -*
import random                       # Ввести модуль случайных чисел
print('start game')
print('you just have three chance to attempt')
randnum=random.randint(1,20)         # Генерация случайного числа от 1 до 20
n=0
while n<3:
    temp=input('please input a number between 1 to 20:')
    num=int(temp)
    if num>20:
        print('error input,input beyond scope')
    else:
        if num<1:
            print()
