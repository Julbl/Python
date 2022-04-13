print("Введите строку: ")
string = input()
print("1.Cимвольный ввод:")
for i in string:
    print(i)
    i += i
result = ""
for i in range(0, len(string)):
    if i != 2:
        result = result+string[i]
print("2.Вывод без третьего символа:", result)
for i in string:
    if i == "c":
        print("В данной строке есть символ 'c'!")
print("3.Длина строки:", len(string))
print("4.Вывод без последнего символа в строке:", string.rstrip(string[-1]))
