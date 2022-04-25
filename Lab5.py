List1 = [str(word1) for word1 in input("Введите через запятую список слов: ").split(', ')]
Set = set(List1)
length = len(Set)
print("Данный список содержит {0} слов".format(length))

print("Заполните второй список с  таким количеством {0} элементов: ".format(length))
List2 = list()
for i in range(1, length + 1, 1):
    List2.append(input("Введите {0} элемент: ".format(i)))

dictionary = {}
for word1, word2 in zip(Set, List2):
    dictionary.setdefault(word1, word2)
print("Словарь: {0}".format(dictionary))
