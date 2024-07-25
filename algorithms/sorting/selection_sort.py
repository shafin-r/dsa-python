# Algorithm to sort an array in an ascending order using Selection Sort.
from array_input import arrayloader

array = arrayloader()
length = len(array)


for i in range(length - 1):
    min_index = i
    for j in range(i+1, length):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print("Sorted Array: ", array)
