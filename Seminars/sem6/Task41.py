# Задача №41. Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод: Ввод:
# 5
# 1 2 3 4 5
# Вывод: 0
# Ввод: 5
# 1 5 1 5 1
# Вывод:  2

list1 = [1, 5, 1, 5, 1, 4, 1, 1, 1]
print(list1)
count = 0
for i in range(1, len(list1) - 1):
    if list1[i - 1] < list1[i] > list1[i + 1]:
        count += 1
print(count)

