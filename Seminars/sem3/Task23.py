# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

list = [0, -1, 5, 2, 3]
i = 1
sum = 0

while i < len(list):
    if list[i] > list[i - 1]:
        sum = sum + 1
    i = i + 1

print(sum)