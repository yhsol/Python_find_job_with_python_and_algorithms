# list = [35, 9, 2, 85, 17]
# result = [2, 9, 17, 35, 85]


def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[min_idx] > a[i]:
            min_idx = i
    return min_idx


def al_selection_sort(a):
    result = []
    while a:
        min_idx = find_min_idx(a)

        value = a.pop(min_idx)
        result.append(value)
    return result


def run():
    d = [2, 4, 5, 1, 3]
    print(al_selection_sort(d))
