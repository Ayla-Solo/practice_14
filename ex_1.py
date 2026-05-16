words = input().split()  # список слов
dictionary = {}

for word in words:
    # если слова ещё нет в словаре
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
sort_words = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
# сортировка по количеству повторений по длине сначала разбив на пары
for word, count in sort_words:
    print(word)