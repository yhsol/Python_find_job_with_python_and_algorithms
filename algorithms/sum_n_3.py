def sum_n_3(n):
  if n <= 1:
    return n
  return n + sum_n_3(n-1)