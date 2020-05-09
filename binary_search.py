def binary_search(a, x):
  start = 0
  end = len(a) - 1

  while start <= end:
    mid = (start + end) // 2
    print("start: ", start)
    print("end: ", end)
    print("mid: ", mid)
    if x == a[mid]:
      return mid
    elif x > a[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return -1