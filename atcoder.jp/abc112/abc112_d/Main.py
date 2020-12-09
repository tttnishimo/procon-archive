n,m=map(int,input().split())
ans=1
for i in range(2,int(m**0.5)+1):
  if m%i==0 and n<=m//i:
    if i>=n:
      ans=max(ans,i,m//i)
    else:
      ans=max(ans,i)
if n==1:
  ans=m
print(ans)