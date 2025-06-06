''' To sort the array we need to take the unsorted array and take any sorting algorithm to sort the array. after the arrays sorted we need to merge the arrays.'''

import sys
import random
def randomargs(n):
    arr = []
    for i in range(n):
       arr.append(random.randint(-99999999, 999999999))
    return arr
def sort(arr):
    # Any sorting algorithm
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def merge_array(arr1, arr2):
    merge = []
    i = j = 0
    # comparison and merging Technique
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append(arr2[j])
            j += 1
    merge.extend(arr1[i:])
    merge.extend(arr2[j:])
    return merge

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pls provide integer on command line")
        sys.exit(1)
    n = int(sys.argv[1])
    arr1 = randomargs(n)
    arr2 = randomargs(n)
    sort_arr1 = sort(arr1)
    sort_arr2 = sort(arr2)

    merge = merge_array(sort_arr1, sort_arr2)
    print(merge)
