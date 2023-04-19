# Даны два числа A и B. Вам нужно вычислить их сумму A+B.
# В этой задаче вам нужно читать из файла и выводить ответ в файл

with open("input.txt", 'r') as infile:
    list1 = infile.read().split()
    print(list1)

    a = int(list1[0])
    b = int(list1[1])
    res = a + b

with open("output.txt", 'w') as outfile:
    outfile.write(str(res))

print(res)
print("Файл сохранен")
