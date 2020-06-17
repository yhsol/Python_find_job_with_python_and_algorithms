def binary_search_2(a, x, start, end):
  if start > end:
    return -1

  mid = (start + end) // 2
  
  if a[mid] == x:
    return mid
  elif a[mid] < x:
    return binary_search_2(a, x, mid + 1, end)
  else:
    return binary_search_2(a, x, start, mid - 1)
  return - 1
  
def binary_search_3(a, x):
  return binary_search_2(a, x, 0, len(a) - 1)