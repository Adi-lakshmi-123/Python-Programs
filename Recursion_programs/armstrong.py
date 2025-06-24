for n in range(1,1001):
    sum=0
    temp=n
    while n!=0:
        r=n%10
        sum=sum+r*r*r
        n=n//10
    if sum==temp:
        print(sum)
