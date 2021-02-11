n=int(input())
a=[int(input()) for _ in range(n)]
ans=[0]*n
for i in range(n):
  if i==0:
    ans[a[i]-1]=100000
  elif i==1:
    ans[a[i]-1]=50000
  elif i==2:
    ans[a[i]-1]=30000
  elif i==3:
    ans[a[i]-1]=20000
  elif i==4:
    ans[a[i]-1]=10000
print(*ans,sep='\n')