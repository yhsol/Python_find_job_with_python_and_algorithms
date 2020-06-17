def sequential_search(n, a):
  for i in a:
    if n == a[i]:
      return i

  return -1