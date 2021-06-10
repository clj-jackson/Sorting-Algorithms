def mergesort(values): # Merge sort
  if len(values) > 1:
    m = len(values)//2
    left_side = values[:m]
    right_side	= values[m:]
    left_side = mergesort(left_side)
    right_side = mergesort(right_side)

    values = []

    while len(left_side) > 0 and len(right_side) > 0:
      if left_side[0] < right_side[0]:
        values.append(left_side[0])
        left_side.remove(left_side[0])
      else:
        values.append(right_side[0])
        right_side.remove(right_side[0])

    for i in left_side:
      values.append(i)
    for i in right_side:
      values.append(i)

  return values
