# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simple(n):

    for i in range(2,n):
        if n % i == 0:
            return "no"
    return "yes"

n = int(input("Введите число: "))
print(simple(n))

# def prime(n):
#     i = 2
#     flag = True
#     while i < n and flag: # расскажите про метод флажка
#         if n % i == 0:
#             flag = False
#         i += 1
#     if flag:
#         return 'yes'
#     return 'no'
#
# n = int(input())
# print(prime(n))