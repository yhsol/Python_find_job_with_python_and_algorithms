def find_min_idx(a):
  n = len(a)
  min_idx = 0
  for i in range(1, n):
    if a[min_idx] > a[i]:
      min_idx = i
  return min_idx
  
def sel_sort(a):
  result = []
  while a:
    # 최솟값 위치를 찾는 함수
    min_idx = find_min_idx(a)
    value = a.pop(min_idx)
    result.append(value)
  return result

d = [2,3,4,1,3]
print(sel_sort(d))