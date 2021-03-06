# Imports
from customerror import custom_error_raiser
from bubble import bubblesort
from insertion import insertionsort
from merge import mergesort
from quick import quicksort
from radix import radixsort
from createlist import create_array
from binarysearch import binarysearch

# Variables
list_ = []

y = input("Would you like to make your own array? \nType any word starting with y if yes, and any word starting with n if you want an autogenerated list.\n\nInput:\t").upper()
y1 = y[0]

if y1 == "Y":
  print("Give the numbers you want for the list one by one here, type any letter once you have finished.\n")
  while True:
    try:
      x = int(input("\n"))
      list_.append(x)
    except:
      break
elif y1 == "N":
  f = int(input("\nHow long would you like the array to be?\nInput:\t"))
  y = int(input("\nWhat value do you want to be the highest possible number?\nInput:\t"))
  print("An array will be made for you now...\n")
  list_ = create_array(f, y)
  print(f"Here is your list:\n{list_}\n")
else:
  cutsom_error_raiser("IncorrectInputError", f"User gave an invalid input\n\nVaild inputs consist of:\nAny input beginning with 'y'\nAny input beginning with 'n'\n\nThe user inputted '{y}'.", "main.py", "31")


# Driver code
sort = input("Which sort would you like to use?\n\nType bubble for bubble sort.\nType insertion for insertion sort.\nType merge for merge sort.\nType quick for quick sort.\nType radix for radix sort.\n\nInput:\t").upper()
sort1 = sort[0]

print(f"\nInitialising {sort} sort...\n\nYour sorted array will be displayed below:\n")

print({"Q": quicksort, "I": insertionsort, "B": bubblesort, "M": mergesort, "R": radixsort}[sort1](list_))

print(f"\nYour {sort} sort has completed.")
