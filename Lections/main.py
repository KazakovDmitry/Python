# # Быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([10,5,2]))

## Сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [3,5,6,9,8,7,13,1,55,2,4]
merge_sort(list1)
print(list1)

# python -m venv venv
# python3 -m venv venv
# venv\Scripts\activate
# РЕШЕНИЕ ДЛЯ WINDOWS - В Windows при установке Python необходимо было установить галочку для установки pip, установить путь Python в папку с:\Program Files, а не в User, и обязательно поставить галочку add PATH
#
# иногнда в винде в командной строке - Set-ExecutionPolicy -ExecutionPolicy AllSigned , если не активируется
#
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#
# вручную надо было добавить pip в Переменную среду Path
# Это в свойствах компьютера надо лазить.
# На Windows 10. Параметры -> Изменение системных переменных среды -> Переменные среды. Потом находим или создаем Path и добавляем путь до pip.
#
# pip freeze
# pip freeze > requirements.txt
#
#
#
# pip install -r requirements.txt