import math
import functools
sg,sh=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(sh):
    sk,sl=map(int,input().split())
    ss=functools.reduce(math.gcd,List[sk-1:sl])
    print(ss)
