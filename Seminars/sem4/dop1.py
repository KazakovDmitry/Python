# 1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
#
# sum = 0
#
# for i in range(len(list)):
#     if i % 2 == 1:
#         sum += list[i]
#
# print(sum)

my_list = [8, 5, 7, 3, 6]
print(sum(my_list[1::2]))