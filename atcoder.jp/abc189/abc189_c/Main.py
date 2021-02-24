n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
  m=a[i]
  for j in range(i,n):
    m=min(m,a[j])
    ans=max(ans,m*(j-i+1))
print(ans)