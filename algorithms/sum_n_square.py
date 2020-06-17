def sum_n_square(n):
  s = 0
  for i in range(1, n+1):
    s = s + i * i
  return s

data = 10
result = sum_n_square(data)
print(result)