def make_pair(a):
  s = set()
  n = len(a)
  for i in range(0, n-1):
    for j in range(i+1, n):
      s.add(a[i] + "-" + a[j])
  return s
  