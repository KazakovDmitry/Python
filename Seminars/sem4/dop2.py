# 2.Напишите программу, которая найдёт произведение пар
# чисел списка.Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.
#
# *Пример: *
# - [2, 3, 4, 5, 6] = > [12, 15, 16];
# - [2, 3, 5, 6] = > [12, 15]

# list1 = list(input("Введите числа через пробел: ").split())
list1 = input("Введите числа через пробел: ").split()
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(list1, end=' ')
list2 = list()
for i in range((len(list1) + 1) // 2):
    list2.append(list1[i] * list1[-i-1])
print('= >', list2)