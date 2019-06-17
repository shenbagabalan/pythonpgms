from math import sqrt
from itertools import count, islice
def isPrime(sh):
    if sh< 2:
        return False
    for number in islice(count(2), int(sqrt(sh) - 1)):
        if sh % number == 0:
            return False
    return True
sh=int(input())
if isPrime(sh):
    print("yes")
else:
    print("no")
