'''Selection Sort Algorithm:

It is one of the sorting technique used to sort the elements in an array. In this selection sorting Algorithm we will follow some steps:

The steps are:

1. First we have to take the unsorted array. Ex: 4,9,10,7,2,19

2. In this find the minimum element in the array. That is 2. Then swap the minimum element with the first element in array. Then the array will be 2,9,10,7,4,19

3. After that in this array 2 is sorted, then we will compare after 2, Then the minimum element is 4. We need to swap the min element(4) with the second element(9). Then the array will be 2,4,10,7,9,19

4. Then the min element in unsorted array is 7. we need to swap this with the third element(10). Then the array will be 2,4,7,10,9,19.

5. Now, The min element in unsorted array is 9. we will swap it with 10. Then the array will be 2,4,7,9,10,19.

6. The array is sorted. The final sorted array is: 2,4,7,9,10,19.
'''

#Algorithm:

import sys
import random

def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def selectionsort(arr):
    for i in range(len(arr)):
        MinElement = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[MinElement]:
                MinElement=j
        arr[i], arr[MinElement] = arr[MinElement], arr[i]
    return arr
if __name__=="__main__":
    arr1 = randomargs(int(input()))
    print(selectionsort(arr1))

