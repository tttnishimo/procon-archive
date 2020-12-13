n,m,t=map(int,input().split())
d=n
flg=0
c=0
for i in range(m):
  a,b=map(int,input().split())
  d-=a-c
  if d<1:
    flg=1
  d=min(n,d-a+b)
  c=b
d-=t-c
if d<1:
  flg=1
if flg==1:
  print('No')
else:
  print('Yes')