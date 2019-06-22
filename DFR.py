sh, se, sk = list(map(str,input().split()))
sk = int(sk)
ct = 0
for i in range(len(sh)):
  if sh[i] != se[i]:
    ct += 1
if ct == sk:
  print("yes")
else:
  print("no")
