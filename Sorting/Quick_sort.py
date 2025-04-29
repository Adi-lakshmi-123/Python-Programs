''' Quick Sort Algorithm:
 1. It is one of the Sorting Technique to arrange the elements in an order.
 2. It is a divide and conquer algorithm. In this we take the array and a pivot value. We can compare left side elememts and right side elements with pivot value. 
   Hence by performing iterations on comparing, we can result the sorted array as output.

   '''

# Algorithm:

import sys
import random
def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot_value = arr[0]
    less_ele = [i for i in arr[1:] if i <= pivot_value]
    greater_ele = [i for i in arr[1:] if i > pivot_value]
    return quicksort(less_ele) + [pivot_value] + quicksort(greater_ele)
    return arr
if __name__ == "__main__":
    if len(sys.argv) == 1:
       print("Pls provide integer on command line")
    lenarr = randomargs(int(sys.argv[1]))
    print(quicksort(lenarr))
