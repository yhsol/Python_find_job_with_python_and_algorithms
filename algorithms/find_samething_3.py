def find_samething_3(a):
  s = set()
  n = len(a)
  for i in range(0, n-1):
    for j in range(i+1, n):
      if a[i] == a[j]:
        s.add(a[i])
  return s