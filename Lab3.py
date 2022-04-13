import math
import random

print("Ноль в качестве знака операции"
      "\nзавершит работу программы")
while True:
    s = input("Выберите знак для нужной вам операции +, -, *, /, ^, random, !, arccos, ||: ")
    if s == '0':
        break
    if s == 'random':
        print("Рандомное число: ", random.random())
    elif s == '!':
        number1 = int(input("Введите число, факториал которого хотите найти: "))
        print("Факториал числа:", math.factorial(number1))
    elif s == 'arccos':
        unit = input("Выберите единицу измерения радиан(1), градус(2):")
        if unit == '1':
            radian = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
            print("Арккосинус числа(радиан): ", math.acos(radian))
        elif unit == '2':
            degrees = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
            print("Арккосинус числа(градусы): ", (math.acos(degrees)*180)/math.pi)
    elif s == '||':
        number2 = float(input("Введите число, модуль которого хотите получить: "))
        print("|", number2, "| = ", abs(number2))
    elif s in ('+', '-', '*', '/', '^'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("x+y =",  x+y)
        elif s == '-':
            print("x-y = ",  x-y)
        elif s == '*':
            print("x*y = ", x*y)
        elif s == '/':
            if y != 0:
                print("x/y = ", x/y)
            else:
                print("Деление на ноль!")
        elif s == '^':
            print("x^y = ", pow(x, y))
    else:
        print("Неверный знак операции!")
