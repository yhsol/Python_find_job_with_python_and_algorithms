def find_samething_2(a):
  s = []
  n = len(a)
  for i in range(0, n):
    print(a[i])
    print(a.count(a[i]))
    if a.count(a[i]) > 1:
      if a[i] not in s:
        s.append(a[i])
  return s