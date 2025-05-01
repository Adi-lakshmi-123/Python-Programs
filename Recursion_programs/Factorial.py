'''
Factorial is used to find the multiplies the given number by integers less or equal to it. 
Ex: Factorial of 5: 5*4*3*2*1=120.
'''
#Program:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = 10
if n < 0:
    print("It is a negative number")
else:
    print(factorial(n))
