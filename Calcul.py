import math
import random

class Calculator:
    @staticmethod
    def printInfo():
        print("Ноль в качестве знака операции"
              "\nзавершит работу программы")

    @staticmethod
    def enterFunction():
        x = float(input("x="))
        y = float(input("y="))
        return x, y

    @staticmethod
    def randomFunction():
        print("Рандомное число: ", random.random())

    @staticmethod
    def factorialFunction():
        number1 = int(input("Введите число, факториал которого хотите найти: "))
        print("Факториал числа:", math.factorial(number1))

    @staticmethod
    def arccosFunction():
        unit = input("Выберите единицу измерения радиан(1), градус(2):")
        if unit == '1':
            radian = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
            print("Арккосинус числа(радиан): ", math.acos(radian))
        elif unit == '2':
            degrees = float(input("Введите число от -1 до 1, арккосинус которого хотите найти: "))
            print("Арккосинус числа(градусы): ", (math.acos(degrees) * 180) / math.pi)

    @staticmethod
    def absFunction():
        number2 = float(input("Введите число, модуль которого хотите получить: "))
        print("|", number2, "| = ", abs(number2))

    @staticmethod
    def plusFunction():
        x, y = Calculator.enterFunction()
        print("{} + {} = {}".format(x, y, x + y))

    @staticmethod
    def minusFunction():
        x, y = Calculator.enterFunction()
        print("{} - {} = {}".format(x, y, x - y))

    @staticmethod
    def multiplicationFunction():
        x, y = Calculator.enterFunction()
        print("{} * {} = {}".format(x, y, x * y))

    @staticmethod
    def divisionFunction():
        x, y = Calculator.enterFunction()
        if y != 0:
            print("{} / {} = {}".format(x, y, x / y))
        else:
            print("Деление на ноль!")

    @staticmethod
    def powerFunction():
        x, y = Calculator.enterFunction()
        print("{} ^ {} = {}".format(x, y, x ** y))

    @staticmethod
    def calculator():
        Calculator.printInfo()
        while True:
            s = input("Выберите знак для нужной вам операции +, -, *, /, ^, random, !, arccos, ||: ")
            if s == '0':
                break
            elif s == '+':
                Calculator.plusFunction()
            elif s == '-':
                Calculator.minusFunction()
            elif s == '*':
                Calculator.multiplicationFunction()
            elif s == '/':
                Calculator.divisionFunction()
            elif s == '^':
                Calculator.powerFunction()
            elif s == 'random':
                Calculator.randomFunction()
            elif s == '!':
                Calculator.factorialFunction()
            elif s == 'arccos':
                Calculator.arccosFunction()
            elif s == '||':
                Calculator.absFunction()
            else:
                print("Неверный знак операции!")