# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
n = int(input("Введите количество оценок в журнале: "))
list1 = [randint(1, 5) for _ in range(n)]
print(*list1)
max_ocenka = max(list1)
print(max_ocenka)
min_ocenka = min(list1)
print(min_ocenka)

for i in range(n):
    if list1[i] == max_ocenka:
        list1[i] = min_ocenka
print(list1)
