import sys

sys.setrecursionlimit(3000)

n = int(input())
m = int(input())
dictionary = {}
# словарь графа:
# ключ = город
# значение = список соседей и расстояний

weight = {}
# словарь расстояний:
# ключ = город
# значение = минимальное расстояние от стартового города


def dijkstra(now_peak, last_peak, dictionary, weight):

    # перебираем соседей текущего города
    for i in dictionary[now_peak]:

        # i[0] — соседний город
        # i[1] — расстояние до него

        if i[0] != now_peak and i[0] in weight:

            # обновляем минимальное расстояние
            weight[i[0]] = min(
                weight[i[0]],
                weight[now_peak] + int(i[1])
            )

    min_peak = ""
    # следующий город для перехода

    min_peak_weight = float("inf")
    # минимальное найденное расстояние

    # ищем город с минимальным расстоянием
    for i in weight:

        if weight[i] < min_peak_weight and i != now_peak:

            min_peak = i
            min_peak_weight = weight[i]

    # если дошли до конечного города
    if min_peak == last_peak:
        return weight[min_peak]

    else:

        del weight[now_peak] # удаляем обработанный город

        now_peak = min_peak # переходим в следующий город

        return dijkstra(now_peak, last_peak, dictionary, weight)

for i in range(m):

    temp_array = list(map(str, input().split(" ")))
    # temp_array[0] — первый город
    # temp_array[1] — второй город
    # temp_array[2] — расстояние

    if temp_array[0] in dictionary:

        dictionary[temp_array[0]] = (
            dictionary[temp_array[0]]
            + [[temp_array[1]] + [temp_array[2]]]
        )
        # добавляем дорогу:
        # город0 → город1

        if temp_array[1] in dictionary:

            dictionary[temp_array[1]] = (
                dictionary[temp_array[1]]
                + [[temp_array[0]] + [temp_array[2]]]
            )
            # добавляем обратную дорогу

        else:

            dictionary[temp_array[1]] = [
                [temp_array[0]] + [temp_array[2]]
            ]

            weight[temp_array[1]] = float('inf')
            # начальное расстояние = бесконечность

    else:

        dictionary[temp_array[0]] = [
            [temp_array[1]] + [temp_array[2]]
        ]

        dictionary[temp_array[1]] = [
            [temp_array[0]] + [temp_array[2]]
        ]
        # создаём дороги в обе стороны

        weight[temp_array[0]] = float('inf')
        weight[temp_array[1]] = float('inf')
        # расстояния пока неизвестны


first_peak, last_peak = map(str, input().split(" "))
# стартовый и конечный город

weight[first_peak] = 0
# расстояние до стартового города = 0

print(dijkstra(first_peak, last_peak, dictionary, weight))
