'''
Factorial is used to find the multiplies the given number by integers less or equal to it. 
Ex: Factorial of 5: 5*4*3*2*1=120.
'''
#Program:
import sys
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Pls provide integer on command line")
    else:
        n=int(sys.argv[1])
        print(factorial(n))
