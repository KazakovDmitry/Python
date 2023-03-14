# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6      0 1 1 2 3 5 8 13

a = int(input("Введите положительное число: "))
count = 3
fibonachi = -1
c = 1
d = 1
while fibonachi < a:
    fibonachi = c + d
    c = d
    d = fibonachi
    count += 1

if fibonachi == a:
    print(count)
else:
    print(-1)

