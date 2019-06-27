t = int(input())
sM = [ int(x) for x in input().split()]
t = len(sM)
sc = 0
for i in range(0,t-2) :
    for j in range(i+1, t-1):
        for k in range(j+1, t):
            if sM[i] > sM[j] > sM[k] :
                sc += 1
print(sc)
