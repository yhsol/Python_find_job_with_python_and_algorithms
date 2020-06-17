def al_max_index(n):
  idx = 0
  n_len = len(n)
  for i in range(0, n_len):
    if n[idx] < n[i]:
      idx = i
  return idx