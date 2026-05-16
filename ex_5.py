def number_of_descendants(name, dictionary):

    # если у человека есть потомки
    if name in dictionary:

        summ = len(dictionary[name])# дети

        for i in dictionary[name]:
            summ += number_of_descendants(i, dictionary) # добавляем потомков ребенка
        return summ

    else:
        return 0

n = int(input())

dictionary = {}
# ключ = родитель
# значение = список детей

for i in range(n):

    temp_array = list(map(str, input().split(" ")))
    # temp_array[0] → родитель
    # temp_array[1] → потомок

    if temp_array[0] in dictionary:
        dictionary[temp_array[0]] = dictionary[temp_array[0]] + [temp_array[1]]
        # добавляем нового ребёнка в список

    else:
        dictionary[temp_array[0]] = [temp_array[1]]
        # создаём новый список детей


name = input()
print(number_of_descendants(name, dictionary))
