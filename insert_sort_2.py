def insert_sort_2(data):
  n = len(data)
  for i in range(1, n):
    key = data[i]
    j = i -1
    while j >= 0 and data[j] > key:
      data[j + 1] = data[j]
      j -= 1
    data[j + 1] = key