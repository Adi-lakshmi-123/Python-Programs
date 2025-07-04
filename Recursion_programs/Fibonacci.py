'''Fibonacci:
Fibonacci is a series of numbers where the number is the sum of its two preceeding numbers. It always starts with 0 and 1.
Ex: 5;  0 1 1 2 3
'''
# Program:
import sys
def fib(n):
    arr = [1, 1]
    if n < len(arr):
       return arr[n]
    for j in range(len(arr), n+1):
        arr.append(arr[j-1] + arr[j-2])
    return arr[n]

if __name__ == "__main__":
    if (len(sys.argv) != 2 ):
       print("sys.argv[0] integer to run the program")
       sys.exit(1)
    print("This is called dynamic programming, faster than recursion")
    print(fib(int(sys.argv[1])))
      
