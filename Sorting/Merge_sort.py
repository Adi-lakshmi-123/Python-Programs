''' Merge Sort Algorithm:
It is one of the sorting technique used to sort the elements in an array. It is a divide and conquer algorithm. In this selection sorting Algorithm we will follow some steps:

The steps are:
1. First take the unsorted array. Ex: 3,12,8,7,6
2. As this is a divide and conquer algorithm. We will divide the array into 2 parts. Each part consists of either 2 or 3 elements.
then array will be 3,12,8   7,6
3. As 3 is less than remaining , we keep same and compare 12 nd 8. 8 should before 12. Then the subarray will be 3,8,12. 
4. The second subarray will be 6,7. As 6 should come before 7.
5. Then we need to merge the 2 subarrays. 3,8,12,6,7.
6. We will arrange in the order. 3,6,8,12,7.
7. After changes the resultant array will be 3,6,7,8,12.

'''
# Algorithm:
import sys
import random
def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def mergesort(arr):
    if len(arr) > 1:
        mid_ele = len(arr) // 2
        left_sub = arr[:mid_ele]
        right_sub = arr[mid_ele:]
        mergesort(left_sub)
        mergesort(right_sub)
        x = y = z = 0
        while x < len(left_sub) and y < len(right_sub):
            if left_sub[x] < right_sub[y]:
                arr[z] = left_sub[x]
                x += 1
            else:
                arr[z] = right_sub[y]
                y += 1
            z += 1

        while x < len(left_sub):
            arr[z] = left_sub[x]
            x += 1
            z += 1

        while y < len(right_sub):
            arr[z] = right_sub[y]
            y += 1
            z += 1
    return arr
if __name__ == "__main__":
    if len(sys.argv) == 1:
       print("Pls provide integer on command line")
       sys.exit(1)
    lenarr = randomargs(int(sys.argv[1]))
    print(mergesort(lenarr))
