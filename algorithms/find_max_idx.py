def find_max_idx(a):
  n = len(a)
  s = 0
  for i in range(1, n):
    if a[s] < a[i]:
      s = i
  return s