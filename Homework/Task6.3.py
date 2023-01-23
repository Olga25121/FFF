# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

#1
words = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

def collection(words):
    new_list = []
    dict_list = {}
    for word in sorted(words):
        key = word[0]
        if key in dict_list:
            dict_list[key].append(word)
        else:
            dict_list[key] = [word]
    return dict_list
print()
print(words)
print()
a = collection (words)
print(a)
print()

#2
from itertools import groupby

list_name = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

def thesaurus(*list_name):
    if "" not in list_name:
        return {k: list(names) for k, names in groupby(sorted(list_name), key=lambda i: i[0]) if k}
    return "Error"
print()
print(list_name)
print()
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))
print()

#3
def thesaurus(*args):
    names_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter not in names_dict:
            names_dict[letter] = [i]
        names_dict[letter] += [i]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Алина", "Бибочка"))

#  ________________________________________________________ 2 вариант
from itertools import groupby


def thesaurus(*args):
    if "" not in args:
        return {ch: list(names) for ch, names in groupby(sorted(args), key=lambda i: i[0]) if ch}
    return "Error"


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))


#  ________________________________________________________ 3 вариант

def thesaurus(*args):
    if "" not in args:
        return {ch[0]: list(filter(lambda el: el.startswith(ch[0]), args)) for ch in sorted(args)}
    return "Error"


thesaurus('Кармен', 'Андрей', 'Василий', 'Алексей', 'Дмитрий', 'Виктор', 'Инна', 'Александра', 'Игнат', 'Спартак',
          'Якоб', 'Люция', 'Дионис', 'Агора', 'Игорь')
