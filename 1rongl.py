nin=int(input())
sl=[int(i) for i in input().split()]
sc=0
for i in range(1,nin-1):
	if sl[i]<sl[i-1] and sl[i]<sl[i+1]:
		sc+=1
	elif sl[i]>sl[i-1] and sl[i]>sl[i+1]:
		sc+=1
print(sc)
