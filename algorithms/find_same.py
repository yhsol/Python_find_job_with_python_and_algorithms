def find_same(a):
  result = []
  s = len(a)
  for i in range(0, s-1):
    for j in range(i + 1, s):
      if a[i] == a[j]:
        if i != j:
          if a[i] not in result:
            result.append(a[i])
  return result