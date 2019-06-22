sh,se = list(map(int,input().split()))
ct = 0
for i in range(1,101):
  if i*i >= sh and i*i <= se:
    ct += 1
print(ct)
