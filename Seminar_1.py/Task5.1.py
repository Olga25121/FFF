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

# import random


# num_words = (int(input("Введите количество слов:\n")))
# def words_list(count): 
#    lst_words = []
#    txt = "абв"
#    for x in range(num_words):
#     if count <= 0:
#         print("Ошибка! Вы ввели отрицательное число")
#         return [-1]
#     random_txt = random.sample(txt, 3)
#     lst_words.append("".join(random_txt))

#     print(" ".join(lst_words))
#     lst_words2 = list(filter(lambda x: txt not in x, lst_words))
#     print(" ".join(lst_words2))

# import random

# num_words = (int(input("Введите количество слов:\n")))
# def generate_random_string(count):
#     text = 'abc'
#     list_words = [''.join(random.choice(text) for i in range(count))]
#     print("Random string of length", count, "is:", list_words)


# generate_random_string(num_words)

# import random
# num_words = (int(input("Введите количество слов:\n")))
# text = [''.join(random.choice('abc') for _ in range('abc'))]
# text[] = random.choice('ABC')

# print(''.join(text))

# text = 'Мы неабв очень любим Питон иабв Джавабв'
# text_find = 'абв'
# index = 0

# list1 = text.split(' ')
# print(list1)

# list2 = [item for item in list1 if text_find not in item]
# print(list2)

# import random 
# num_words = int(input("Введите количество слов:\n"))
# def words_list(count):   
#     text = 'abc' 
#     list_in = []
#     if count <= 0:
#         print("Ошибка! Вы ввели отрицательное число")
#         return [-1]
#     for x in range(num_words):
#         txt = random.sample(text, 3)
#         list_in.append(' '.join(txt))
#     print(' '.join(list_in))
    
# #     for i in range(count):
# #         list_in.append(round(choices('abc')))
# #     return list_in
#     res = list(filter(lambda x: text not in x, list_in))
#     print(' '.join(res))
# num_words = input("Введите количество слов:\n")
# def words_list(count):    
    
#     if count <= 0:
#         print("Ошибка! Вы ввели отрицательное число")
#         return [-1]
# words = input("Введите текст через пробел:\n")
# print([words])
# list_in = ['abc']
# lst = [i for i in words.split() if list_in not in i]
# print([' '.join(lst)])
import random

txt = "абв"
print("Слово которое нужно удалить из текста: ", txt)
num_word = (int(input("Количество слов в тексте: ")))
list_word = []
print("Рандомный текст: ")
for x in range(num_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

print("Текст без абв: ")
list_word2 = list(filter(lambda x: txt not in x, list_word))
print(" ".join(list_word2))