def counting_subroutine(x, y): # Couting sort - Subroutine
  
  n = len(x) 
  f = [0] * (n)  
  z = [0] * (10) 

  for i in range(0, n): 
    index = (x[i] / y) 
    z[int(index % 10)] += 1 
  for i in range(1, 10): 
    z[i] += z[i - 1] 
  i = n - 1
  while i >= 0: 
    index = (x[i] / y) 
    f[z[int(index % 10)] - 1] = x[i] 
    z[int(index % 10)] -= 1
    i -= 1
  i = 0
  for i in range(0, len(x)): 
    x[i] = f[i] 

def radixsort(x): # Radix sort
  max_ = max(x) 
  y = 1
  while max_ / y > 0: 
    counting_subroutine(x, y) 
    y *= 10
  return x

