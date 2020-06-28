def al_sequential_search(a, s):
    n = len(a)
    results = []
    for i in range(0, n):
        if a[i] == s:
            results.append(i)
    return results


def search_by_index(a, s, n):
    key = al_sequential_search(a, s)[0]
    return n[key]
