sh, se = list(map(int,input().split()))
for i in range(se,0,-1):
  if sh%i == 0 and se%i == 0:
    print(i)
    break
