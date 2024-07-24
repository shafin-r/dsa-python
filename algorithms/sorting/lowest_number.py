# Algorithm to find the lowest number in an array.
from array_input import arrayloader

array = arrayloader()
lowest = array[0]
for item in array:
    if item < lowest:
        lowest = array[item]
print(f"The lowest number is {lowest}.")