for n in range(101,1000):
    rev = 0
    x = n
    while n!=0:
        r = n%10
        rev = (rev*10) + r
        n = n//10
    if x == rev:
        print(rev)
