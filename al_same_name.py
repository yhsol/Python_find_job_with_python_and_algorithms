def al_same_name(n):
  results = set()
  n_len = len(n)
  for i in range(0, n_len-1):
    for j in range(i+1, n_len):
      if n[i] == n[j]:
        results.add(n[i])
  return results
  