sh=list(map(int,input().split()))
for i in range(1,(sh[0]*sh[1])+1):
    if(i%sh[0]==0 and i%sh[1]==0):
        print(i)
        break
