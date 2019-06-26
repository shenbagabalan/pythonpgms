from itertools import combinations
sh,se=map(int,input().split())
sg=len(str(sh))
sa=list(combinations(str(sh),sg-se))
sa=(sorted(sa))
sl="".join(sa[0])
print(sl)
