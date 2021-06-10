from random import randint

def create_array(x, y): # List generator
  array = []
  for i in range(0, x):
    array.append(randint(1, y))
  return array
