N,Q=map(int,input().split())
a=[0]*(N+1)
for i in range(Q):
  l,r,x=map(int,input().split())
  a[l-1]+=x
  a[r]-=x
ans=''
for i in range(1,N):
  a[i]+=a[i-1]
  if a[i-1]>a[i]:
    ans+='>'
  elif a[i-1]<a[i]:
    ans+='<'
  else:
    ans+='='
print(ans)