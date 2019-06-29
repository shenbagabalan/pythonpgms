ns = int(input())
b = []
ain = ns//2 + ns
for i in range(1,ns+1):
  if i%2==0:
    b.append(i)
for i in range(1,ns+1):
  if i%2!=0:
    b.append(i)
for i in range(1,ns+1):
  if i%2==0:
    b.append(i)
print(ain)
print(*b)
