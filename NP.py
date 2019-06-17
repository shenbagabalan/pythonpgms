from math import sqrt
from itertools import count, islice
def isPrime(sh):
    if sh < 2:
        return False
    for number in islice(count(2), int(sqrt(sh) - 1)):
        if sh % number == 0:
            return False
    return True
o,e=map(int,input().split())
s=[]
for i in range(o+1,e):
    if isPrime(i):
        s.append(i)
    
print(*s)
