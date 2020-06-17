def al_factorial(data):
  results = 1
  for i in range(1, data+1):
    results = results * i
  return results

results = al_factorial(5)

def run():
  return al_factorial(5)