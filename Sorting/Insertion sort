''' Insertion sort Algorithm:
It is one of the sorting technique used to sort the elements in an array. In this Insertion sorting Algorithm we will follow some steps:

The steps are:
1. First we need to take the unsorted array to sort it using the algorithm.Let us take 50,30,10,20,40.

2. Now we compare the second element with the first element. As 30<50. We need to move the places. Then array will be 30,50,10,20,40.

3. After that we will compare the third element with the first element, As 10<30. Move 10 to 1st position. Then array is 10,30,50,20,40.

4. Then As 10 is sorted, we need to compare 4th element with the second element. As 20<30. move the position of 20 to second position. Then array will be 10,20,30,50,40.

5. The array is sorted upto 3 positions,then we will compare 50 and 40, As 40<50. We will move the positions. Then array will be 10,20,30,40,50.

6. The Sorted array is 10,20,30,40,50.
'''
#Algorithm:

import sys
import random

def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def insertionsort(arr):
    for i in range(1,len(arr)):
        currentEle = arr[i]
        j = i-1
        while j >= 0 and currentEle < arr[j]:
                arr[j-1]=arr[j]
                j-=1
        arr[j+1]=currentEle
    return arr
if __name__ == "__main__":
    if len(sys.argv) == 1:
       print("Pls provide integer on command line")
    lenarr = randomargs(int(sys.argv[1]))
    print(selectionsort(lenarr))
