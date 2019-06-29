sh,bi=list(map(int,input().split()))
cin,din=list(map(int,input().split()))
ein,fin=list(map(int,input().split()))
gin,hin=list(map(int,input().split()))
mh=din-bi
nh=fin-hin
oh=ein-cin
ph=gin-sh
if (mh==nh==oh==ph):
    print("yes")
else:
    print("no")
