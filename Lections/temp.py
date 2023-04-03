d = ['а', 'ы', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и']

text = input("Введите стих: ") # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# #Фразы отделяются друг от друга пробелами.
list_of_words = text.split()

list_result = []
for i in range(len(list_of_words)):
    list_result.append(0)
    for j in d:
        list_result[i] += list_of_words[i].count(j)
        # list_result.append(i.count(j))
        print(list_of_words[i], list_of_words[i].count(j), j)

print("Количество гласных в словах:", list_result)

def find_vowels(characteristic, objects):
    for i in range(len(list_result) - 1):
        if(list_result[i]) !=(list_result[i + 1]):
            return False
    return True


print("Парам пам-пам") if find_vowels(list_result, list_of_words) else print("Пам парам")