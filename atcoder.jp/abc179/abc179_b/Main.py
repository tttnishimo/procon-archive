n=int(input())
zoro=0
flg=0
for i in range(n):
  a,b=map(int,input().split())
  if a==b:
    zoro+=1
  else:
    zoro=0
  if zoro==3:
    flg=1
if flg==1:
  print('Yes')
else:
  print('No')