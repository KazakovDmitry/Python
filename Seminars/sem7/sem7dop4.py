# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
print(list1)
find_str = input("Что ищем? ")
count = 0
flag = True
i = 0
while flag:
    if i >= len(list1) and count < 2:
        print('-1')
        flag = False
    elif find_str == list1[i]:
        count += 1
    if count == 2:
        print(i)
        flag = False
    i += 1
    
