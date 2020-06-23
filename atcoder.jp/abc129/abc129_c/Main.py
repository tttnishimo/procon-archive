n,m=map(int,input().split())
a=[1]*(n+1)
flg=0
for i in range(m):
  a[int(input())]=-1
for i in range(2,n+1):
  if a[i]==-1:
    pass
  elif a[i-1]==-1 and a[i-2]==-1:
    flg=1
    break
  elif a[i-1]==-1:
    a[i]=a[i-2]
  elif a[i-2]==-1:
    a[i]=a[i-1]
  else:
    a[i]=a[i-1]+a[i-2]
if flg==1:
  print(0)
else:
  print(a[-1]%1000000007)