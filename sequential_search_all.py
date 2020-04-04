def sequential_search_all(a, n):
  array = []
  list_n = len(n)
  for i in range(0, list_n):
    if a == n[i]:
      array.append(i)
  return array
  