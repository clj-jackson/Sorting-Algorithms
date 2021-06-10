"""
This file has functions for a bubble sort and a random list GeneratorExit

Using the bubble_sort() function:

bubble_sort(*put the variable name or the list you want to be sorted*)

Using the get_random_list() function:

get_random_list(*put the length of the list you want*, *put the range of the list you want from 0,x*)
"""

from random import randint
from customerror import custom_error_raiser

def bubblesort(the_list): # This function runs a bubble sorting algorithm
  swapped = True # This is used to determine whether the list is already sorted or not
  length_remover = -1 # Decreases the length fo the for loop
  while swapped:
    swapped = False
    length_remover += 1
    for current in range(len(the_list)-1-length_remover): # In the for loop is when the swapping occurs
      if the_list[current] > the_list[current+1]: # Swaps the values
        the_list[current], the_list[current+1] = the_list[current+1], the_list[current]
        swapped = True
  return the_list # The output of the function
