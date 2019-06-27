st,ss=map(int,input().split())
sn=0
Li=[]
for i in range(st):
      Li.append(input())
for i in range(st):
      for j in range(ss-1):
            if(Li[i][j]!='R' and Li[i][j+1]!='R'):
                  sn+=3
            elif(Li[i][j]!='G' and Li[i][j+1]!='G'):
                  sn+=5
print(sn)
