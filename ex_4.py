n = int(input())
dictionary = {}
# ключ = предмет
# значение = форма предмета

for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    # temp_array[0] — форма
    # temp_array[1:] — предметы этой формы

    for i in range(1, len(temp_array)):
        dictionary[temp_array[i]] = temp_array[0]
        # предмет → форма
subject = input()

print(dictionary.get(subject))
