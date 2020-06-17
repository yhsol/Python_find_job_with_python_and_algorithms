def find_in_two_list(a, list1, list2):
  n1 = len(list1)
  for i in range(0, n1):
    if a == list1[i]:
      return list2[i]

  return "?"