# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

a = [1, 1, 2, 0, -1, 3, 4, 4]

for i in range(len(a)):
    for j in range(i + 1, len(a) - 1):
        if a[j] == a[i]:
            a.pop(j)
        print(a)
if a[len(a) - 2] == a[len(a) - 1]:
    a.pop(len(a) - 1)
print(a)
print(len(a))