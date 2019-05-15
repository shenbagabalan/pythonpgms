yrsk=int(input())
if((yrsk%400==0) or (yrsk%4==0) and (yrsk%100!=0)):
    print("yes")
else:
    print("no")
