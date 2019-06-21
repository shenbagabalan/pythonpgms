sh=int(input())
for sz in range(2,sh+1):
  if(sh%sz==0):
      st=0
      for i in range(2,sz+1):
          if(sz%i==0) and (i!=sz):
              st=1
              break
      if(st==0):
          print(sz,end=' ')
