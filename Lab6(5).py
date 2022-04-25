def createList1():
    return [str(word1) for word1 in input("Введите через запятую список слов: ").split(', ')]


def SetAndLength(List1):
    Set = set(List1)
    Length = len(Set)
    print("Данный список содержит {0} слов".format(Length))
    return Set


def createList2(length):
    print("Заполните второй список с  таким количеством {0} элементов: ".format(length))
    List2 = list()
    for i in range(1, length + 1, 1):
        List2.append(input("Введите {0} элемент: ".format(i)))
    return List2


def createDictionary(words1, words2):
    dictionary = {}
    for word1, word2 in zip(words1, words2):
        dictionary.setdefault(word1, word2)
    return dictionary


def main():
    List1 = createList1()
    Set = SetAndLength(List1)
    List2 = createList2(len(Set))
    Dictionary = createDictionary(Set, List2)
    print("Словарь: {0}".format(Dictionary))


main()
