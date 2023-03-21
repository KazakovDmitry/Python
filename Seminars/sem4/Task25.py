# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

list_1 = input("Введите символы через пробел: ").split()
print(*list_1)
dict = {}
for i in range(len(list_1)):
    if list_1[i] in dict.keys():
        dict[list_1[i]] += 1
        list_1[i] = list_1[i] + f'_{dict[list_1[i]]}'
    else:
        dict[list_1[i]] = 0
print(dict)
print(*list_1)

# string = input('Введите строку: ').split()
# letter_dict = {}
# result_string = []
# for letter in string:
#     if letter in letter_dict.keys():
#         result_string.append(f'{letter}_{letter_dict[letter]}')
#     else:
#         result_string.append(letter)
#     letter_dict[letter] = letter_dict.get(letter, 0) + 1
#
# print(' '.join(result_string))