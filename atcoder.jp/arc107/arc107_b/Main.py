n,k=map(int,input().split())
a=[i+1 for i in range(n)]
for i in range(n-1):
  a.append(n-i-1)
ans=0
for i in range(2*n-1):
  if i+k<0 or i+k>2*n-2:
    pass
  else:
    ans+=a[i]*a[i+k]
print(ans)