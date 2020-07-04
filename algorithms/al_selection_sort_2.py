def al_selection_sort_2(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                # print("j: ", j, "min_idx: ", min_idx)
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)


def run():
    d = [2, 4, 5, 1, 3]
    al_selection_sort_2(d)
    print(d)
