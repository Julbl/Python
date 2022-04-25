import math
import random


def printInfo():
    print("Ноль в качестве знака операции"
          "\nзавершит работу программы")


def enterFunction():
    x = float(input("x="))
    y = float(input("y="))
    return x, y


def randomFunction():
    print("Рандомное число: ", random.random())


def factorialFunction():
    number1 = int(input("Введите число, факториал которого хотите найти: "))
    print("Факториал числа:", math.factorial(number1))


def arccosFunction():
    unit = input("Выберите единицу измерения радиан(1), градус(2):")
    if unit == '1':
        radian = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
        print("Арккосинус числа(радиан): ", math.acos(radian))
    elif unit == '2':
        degrees = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
        print("Арккосинус числа(градусы): ", (math.acos(degrees) * 180) / math.pi)


def absFunction():
    number2 = float(input("Введите число, модуль которого хотите получить: "))
    print("|", number2, "| = ", abs(number2))


def plusFunction():
    x, y = enterFunction()
    print("{} + {} = {}".format(x, y, x + y))


def minusFunction():
    x, y = enterFunction()
    print("{} - {} = {}".format(x, y, x - y))


def multiplicationFunction():
    x, y = enterFunction()
    print("{} * {} = {}".format(x, y, x * y))


def divisionFunction():
    x, y = enterFunction()
    if y != 0:
        print("{} / {} = {}".format(x, y, x / y))
    else:
        print("Деление на ноль!")


def powerFunction():
    x, y = enterFunction()
    print("{} ^ {} = {}".format(x, y, x ** y))


def calculator():
    printInfo()
    while True:
        s = input("Выберите знак для нужной вам операции +, -, *, /, ^, random, !, arccos, ||: ")
        if s == '0':
            break
        elif s == '+':
            plusFunction()
        elif s == '-':
            minusFunction()
        elif s == '*':
            multiplicationFunction()
        elif s == '/':
            divisionFunction()
        elif s == '^':
            powerFunction()
        elif s == 'random':
            randomFunction()
        elif s == '!':
            factorialFunction()
        elif s == 'arccos':
            arccosFunction()
        elif s == '||':
            absFunction()
        else:
            print("Неверный знак операции!")


calculator()