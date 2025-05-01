'''Fibonacci:
Fibonacci is a series of numbers where the number is the sum of its two preceeding numbers. It always starts with 0 and 1.
Ex: 5;  0 1 1 2 3
'''
# Program:
import sys
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pls provide integer on command line")
    else:
        n=int(sys.argv[1])
        for i in range(n):
            print(fibonacci(i))
      
