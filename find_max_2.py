def find_max_2(a, n):
  if n == 1:
    return a[0]

  s = find_max_2(a, n-1)
  if s > a[n - 1]:
    return s
  else:
    return a[n - 1]
  