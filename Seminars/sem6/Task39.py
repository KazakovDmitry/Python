# Задача №39. Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод (каждое число вводится с новой строки): 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод: 3 3 2 12

def fill_array(n):
    list1 = list()
    for i in range(n):
        list1.append(int(input("Введите элемент массива: ")))
    return list1

n = int(input("Введите количество элементов в первом массиве: "))
list_n = fill_array(n)
print(list_n)

m = int(input("Введите количество элементов в первом массиве: "))
list_m = fill_array(m)
print(list_m)

i = 0
while i < len(list_n):
    flag = True
    j = 0
    while flag and j < m:
        if list_m[j] == list_n[i]:
            list_n.pop(i)
            flag = False
        j += 1
    i += 1

print(list_n)

def find_repeat_element(a, b, i = 0): 
    if i < len(a):
        if len(b) <= 1:
            if b[0] == a[0]:
                a.pop(0)            
            return a
        return find_repeat_element(a, b[1:], i = 0)
    return find_repeat_element(a, b, i = i + 1)

print('рекурсия:', find_repeat_element(list_n, list_m))