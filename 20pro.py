ns, ms = list(map(int, input().split()))
c = 0
for l in range(ns, ms+1):
    t = (bin(l)[2:]).count('1')
    if t == 1:
        continue
    for n in range(2, t):
        if t % ns == 0:
            flag = False
            break
    else:
        c += 1
print(c)
