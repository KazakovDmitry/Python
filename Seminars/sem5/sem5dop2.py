# Проверка палиндрома. Напишите функцию, которая проверяет, является ли строка палиндромом
# (то есть читается одинаково справа налево и слева направо) с использованием рекурсии.

def palindrome(a):
    if len(a) == 0 or len(a) == 1:
        return print('Это палиндром')
    if a[0] == a[-1]:
        palindrome(a[1:-1])
    else:
        return print('Это НЕ палиндром')

a = input("Введите текст: ")
palindrome(a)