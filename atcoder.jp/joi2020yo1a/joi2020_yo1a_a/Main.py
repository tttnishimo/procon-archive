a,b,c=map(int,input().split())
flg=0
if a==1:
  flg+=1
if b==1:
  flg+=1
if c==1:
  flg+=1
if flg==3 or flg==2:
  print(1)
else:
  print(2)