sh=int(input())
se=list(map(int,input().split()))
avg=int(sh/2)
lb1=se[:avg]
lb2=se[avg::]
if ((sum(lb1)//len(lb1))==(sum(lb2)//len(lb2))):
    print("yes")
else:
    print("no")
