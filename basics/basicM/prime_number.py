import math


def prime_number( n):
    n=int(n)
    if n <=1:
        return False
    if n ==2 or n==3 :
        return True
    if n>=3 and n%3==0 or n%2==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,6):
        if n%i==0 or n%i+2==0:
            return False
    return True

print(f"{prime_number(11)}")
print(f"{prime_number(3)}")
print(f"{prime_number(17)}")