sh=int(input())
se,si=map(int,input().split())
for i in range(se+1,si):
    if(i==sh):
        print('yes')
        break
else:
    print('no')
