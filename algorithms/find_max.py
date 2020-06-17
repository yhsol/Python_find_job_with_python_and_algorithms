def find_max(a):
  n = len(a)
  s = a[0]
  for i in range(1, n):
    if s < a[i]:
      s = a[i]
  return s

v = [17,92,18,33,58,7,33,44]
print(find_max(v))