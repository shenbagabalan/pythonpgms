sh=int(input())
se=list(map(int,input().split()))
st=se[:]
st.sort()
for i in range(0,len(se)):
  if(se[i]!=st[i]):
     print(i)
     break
