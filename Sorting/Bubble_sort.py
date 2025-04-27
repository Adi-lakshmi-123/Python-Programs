''' Bubble Sort Algorithm:

It is one of the sorting technique used to sort the elements in an array. In this selection sorting Algorithm we will follow some steps:
The steps are:
1. First we have to take the unsorted array. Ex: 4,9,10,7,2,1.
2. We need to compare the adjacent elements to sort the array. First compare 4 and 9. As 9>4. We do not perform the swapping as they are in order.
3. Upto 10, the array is sorted, then we will compare 10 and 7, As 7<10, then swap them. The array will be 4,9,7,10,2,1.
4. After that we will compare 10 and 2 and swap them. The array will be 4,9,7,2,10,1.
5. Then we will compare 10 and 1 and swap them. the array will be 4,9,7,2,1,10.
6. After that we will swap 9 and 7. then array will be 4,7,9,2,1,10.
7. Again compare 9 and 2. and swap. The array is 4,7,2,9,1,10.
8. And compare 9 and 1 and swap. The array is 4,7,2,1,9,10.
9. Now we compare 2 and 1 and swapping occurs. The array is 4,7,1,2,9,10.
10. After many swaps The resultant array will be 1,2,4,7,9,10.

'''

# Algorithm

import sys
import random
def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pls provide integer on command line")
    lenarr = randomargs(int(sys.argv[1]))
    print(bubblesort(lenarr))
