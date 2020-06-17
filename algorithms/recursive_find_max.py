def recursive_find_max(a, n):
  if n == 1:
    return a[0]
  max_n_1 = recursive_find_max(a, n-1)
  if max_n_1 > a[n-1]:
    return max_n_1
  else:
    return a[n-1]

v = [17,92,18,33,58,7,33,42,10]
result = recursive_find_max(v, len(v))