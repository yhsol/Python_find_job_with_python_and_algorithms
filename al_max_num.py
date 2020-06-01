def al_max_num(n):
  n_len = len(n)
  result = n[0]
  print("len",n_len)
  print("n: ", n[4])
  for i in range(0, n_len):
    print("i in for: ", i)
    if result < n[i]:
      result = n[i]
  return result