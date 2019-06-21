sh = [int(i) for i in input().split()]
sh1 = [int(i) for i in input().split()]
sh2=''
for i in range(0,sh[1]):
  sh1 = [sh1[-1]] + sh1[:-1]
print(*sh1,sep=' ')
