# Algorithm to sort an array in an ascending order using Bubble Sort.
from array_input import arrayloader

array = arrayloader()

for i in range(len(array) - 1):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print("Sorted Array: ", array)
        
        


