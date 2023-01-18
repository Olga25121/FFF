# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE

# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

# https://www.youtube.com/watch?v=q_N2Y6-O1xw&ab_channel=dinsky

#1
with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст, необходимый для сжатия: '))
with open('text_words.txt', 'r') as file:
    text = file.readline()
    txt_compress = text.split()

print()
def coding(txt):
    count = 1
    res = ''
    if not txt:
        return ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

txt_compress = coding(text)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compress}')

# Можно вывести результат в консоль

print(f"Текст после кодировки: {coding(text)}")
print(f"Текст после дешифровки: {decoding(coding(text))}")

#2
from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():   # '22a6b'
                    if i.isdigit():   
                        n += i        # n = '22' приплюсовывает
                    else:
                        word_nums.append([int(n), i]) # [22, 'a']
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums))) # 22*a перемножает
    else:
        print("The files do not exist in the system!")

# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             for i in my_f:
#                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
#                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
#     else:
#         print("The files do not exist in the system!")

# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decode(input("Enter the name of the file to decode: "))