# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#  В тексте используется разделитель пробел.
# in -> Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in -> Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in -> Number of words: -1
# out
# The data is incorrect

#1
import random

def words_list(count):    
    txt = "абв"
    lst1 = []
    if count <= 0:
        print("Ошибка! Вы ввели отрицательное число.")
        
    for x in range(count):
        random_txt = random.sample(txt, 3) # k = 3
        lst1.append("".join(random_txt))
    return(' '.join(lst1))
     
def new_list(lst1):
    ex = "абв"
    list2 = [item for item in lst1.split() if ex not in item]
    print(" ".join(list2))
    
result = words_list(int(input("Введите длину списка: ")))
print(result) 
print()
print("Список без слов 'абв': ")
print(new_list(result))

#2
from random import sample

def words_list(count):
    txt = "абв"
    lst1 = []
    if count <= 0:
        print("Ошибка! Вы ввели отрицательное число.")
        return 0
    for x in range(count):
        random_txt = sample(txt, k=3)
        lst1.append("".join(random_txt))
    return ' '.join(lst1)
def new_list(lst1):
    if lst1:
        ex = "абв"
        list2 = [item for item in lst1.split() if ex not in item]
        return " ".join(list2)
    return ''

result = words_list(int(input("Введите длину списка: ")))
print(result)
print()
print("Список без слов 'абв': ")
print(new_list(result))

#3
from random import sample


def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)


# def list_rand_words(count: int, alp: str = 'абв'):                       # list comprehention
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))


def simple_sentence(words: str) -> str:
    # return " ".join(words.replace("абв", "").split())
    return " ".join(i for i in words.split() if i != "абв")


all_list = list_rand_words(int(input("Number of words: ")))
print(all_list)
print(simple_sentence(all_list))