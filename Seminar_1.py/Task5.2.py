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

with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст, необходимый для сжатия: '))
with open('text_words.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

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

txt_compr = coding(my_txt)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')

# Можно вывести результат в консоль
# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(my_txt)}")
# print(f"Текст после дешифровки: {decoding(coding(my_txt))}")