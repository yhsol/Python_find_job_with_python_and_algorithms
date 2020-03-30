def find_samething(a):
  s = []
  n = len(a)
  for i in range(0, n-1):
    for j in range(1, n):
      if a[i] == a[j]:
        if i != j:
          if a[i] not in s:
            s.append(a[i])
  return s