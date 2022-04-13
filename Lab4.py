string1 = str(input("Введите название овоща: "))
string2 = str(input("Введите название овоща: "))
string3 = str(input("Введите название овоща: "))

print("В нижнем регистре:")
print(string1.lower())
print(string2.lower())
print(string3.lower())

print("В верхнем регистре:")
print(string1.upper())
print(string2.upper())
print(string3.upper())

print("С заглавной буквы:")
print(string1.capitalize())
print(string2.capitalize())
print(string3.capitalize())

amount1 = int(input("Введите колличество первой позиции:"))
amount2 = int(input("Введите колличсество второй позиции:"))
amount3 = int(input("Введите колличсество третьей позиции:"))

print("Количество позиции '{}' равняется: {}".format(string1, amount1).capitalize())
print("Количество позиции '{}' равняется: {}".format(string2, amount2).capitalize())
print("Количество позиции '{}' равняется: {}".format(string3, amount3).capitalize())
