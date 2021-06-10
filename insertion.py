def insertionsort(thelist): # Insertion sort
  for i in range(1, len(thelist)):
    x = thelist[i]
    j = i - 1
    while j >= 0 and x < thelist[j]:
      thelist[j + 1] = thelist[j]
      j = j - 1
    thelist[j + 1] = x
  return thelist

