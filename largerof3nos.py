value1,value2,value3=input().split()
value1=int(value1)
value2=int(value2)
value3=int(value3)
if(value1>value2 and value1>value3):
    print(value1)
elif(value2>value3):
    print(value2)
else:
    print(value3)
