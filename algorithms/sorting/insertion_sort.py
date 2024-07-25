# Algorithm to sort an array in an ascending order using Insertion Sort.
from array_input import arrayloader

array = arrayloader()
length = len(array)

for i in range(1, length):
    insert_index = i
    current_value = array[i]
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            array[j+1] = array[j]
            insert_index = j
        else:
            break
    array[insert_index] = current_value

print("Sorted Array: ", array)
