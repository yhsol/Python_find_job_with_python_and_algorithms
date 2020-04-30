def find_ins_idx(r, v):
  for i in range(0, len(r)):
    if r[i] > v:
      return i
  return len(r)

def insert_sort(a):
  result = []
  while a:
    value = a.pop(0)
    ins_idx = find_ins_idx(result, value)
    result.insert(ins_idx, value)
  return result