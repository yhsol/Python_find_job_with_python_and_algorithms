def find_min_idx(a):
  n = len(a)
  min_idx = 0
  for i in range(0, n-1):
    if a[min_idx] > a[i]:
      min_idx = i
  return min_idx


def sel_sort(a):
  result = []
  while a:
    min_idx = find_min_idx(a)
    value = a.pop(min_idx)
    result.append(value)
  return result
