sh=int(input())
si=[]
for i in range(0,sh):  
    ds=input()
    si.append(ds)
list=[]
for i in zip(*si):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
