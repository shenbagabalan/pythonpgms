st=int(input())
za=[]
k=bin(2**st-1)[2::]
l=len(k)
for i in range(0,2**st):
    sf=bin(i)[2::]
    if len(sf)<l:
        za.append([sf.count("1"),(l-len(sf))*"0"+sf])
    else:
        za.append([sf.count("1"),sf])
za.sort()
for i in range(0,len(za)):
    print(za[i][1])
