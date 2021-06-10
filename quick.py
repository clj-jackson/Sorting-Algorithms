from statistics import median

def quicksort(x): # Quick sort
  piv_points = []
  left = []
  equal = []
  right = []

  if len(x) > 1:
    piv_points.append(x[0])
    piv_points.append(x[len(x)//2])
    piv_points.append(x[len(x)-1])
    pivot = median(piv_points)
    for x in x:
      if x < pivot:
        left.append(x)
      elif x == pivot:
        equal.append(x)
      elif x > pivot:
        right.append(x)
    return quicksort(left) + equal + quicksort(right)
  else:
    return x
