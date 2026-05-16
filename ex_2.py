n = int(input())
dictionary = {}
for i in range(n):
    temp_array = list(map(str, input().split(" ")))
    # русское слово и английский перевод
    dictionary[temp_array[0]] = temp_array[1]
    # ключ = русское слово
    # значение = английское слово

translate = list(map(str, input().split(" ")))
# считываем фразу для перевода и разбиваем на слова

translation = ""
# строка, в которой будем собирать перевод

for i in range(len(translate)):
    translation += dictionary.get(translate[i], translate[i]) + " "
    # берётся перевод или берётся само слово без изменений
print(translation)