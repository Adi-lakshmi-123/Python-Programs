#Perfect Number:

'''A perfect number is a positive integer that is equal to the sum of its positive divisors, that is, the sum of its positive divisors except the number itself. Also a perfect number is a number that is half the sum of all
of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its positive divisors,
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors:
( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is about the Perfect Number.
'''
#Program:

def perfectNum(n):
    sum = 0
    for x in range(1, n):
        '''Finding The factors of a number'''
        if n % x == 0:
            sum += x
    return sum == n

if __name__ == "__main__":
    print(perfectNum(6)) 
    print(perfectNum(3)) 
