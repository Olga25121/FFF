# 5. ** Даны два файла, в каждом из которых находится запись многочленов. 
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0

# in
# "poly.txt"
# "poly_2.txt"

# out
# The contents of the files do not match!

from random import choice


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first = my_f_1.readlines()
        second = my_f_2.readlines()

        if len(first) == len(second):
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i, v in enumerate(first):
                    my_f_3.write(f"{v[:-5]} + {second[i]}")
        else:
            print("The contents of the files do not match!")


# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")

#2
# ---------------------------------- сложный вариант

from random import choice


def poly_sum(name_1: str, name_2: str):
    with open(name_1, "r", encoding="utf-8") as my_f_1, \
            open(name_2, "r", encoding="utf-8") as my_f_2:
        first, second = my_f_1.readlines(), my_f_2.readlines()

        if len(first) == len(second):
            with open("sum_poly.txt", "a", encoding="utf-8") as my_f_3:
                for i in range(len(first)):
                    f_list, s_list = sorted([first[i].split(), second[i].split()], key=len, reverse=True)

                    end_first, end_second = f_list[-4:-2], s_list[-4:-2]

                    f, s = f_list[:-4], s_list[:-4]
                    f.insert(0, "+")
                    s.insert(0, "+")

                    f = [f[d - 1] + f[d] for d in range(1, len(f), 2) if d != 0]
                    s = [s[p - 1] + s[p] for p in range(1, len(s), 2) if p != 0]

                    first_dict = {j[j.index("x"):]: j[:j.index("*")] for j in f}
                    second_dict = {j[j.index("x"):]: j[:j.index("*")] for j in s}

                    dict_max = max(first_dict, second_dict, key=len)
                    dict_min = min(second_dict, first_dict, key=len)

                    # print(dict_max)
                    # print(dict_min)

                    result_list = {k: f"{int(v) + int(dict_max[k])}" if k in dict_max and k in dict_min
                                   else v for k, v in (dict_max | dict_min).items()}

                    # print(result_list)

                    n = [f"+ {int(v)}*{k} " if int(v) > 0 else f"{v[0]} {v[1:]}*{k} "
                         for k, v in result_list.items() if v != "0"]

                    # print(n)

                    sum_of_last = eval(''.join(end_first + end_second))
                    n.append(f"+ {sum_of_last} = 0\n" if sum_of_last > 0 else f"- {abs(sum_of_last)} = 0\n")

                    my_f_3.writelines(n)
        else:
            print("The contents of the files do not match!")


# poly_sum(input("Enter the file name 'text_1.txt': "), input("Enter the file name 'text_2.txt': "))
poly_sum("poly.txt", "poly_2.txt")
