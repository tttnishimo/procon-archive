n,m=map(int,input().split())
a=list(map(int,input().split()))
a.append(0)
a.append(n+1)
a.sort()
k=n
ans=0
b=[]
for i in range(len(a)-1):
  if a[i+1]-a[i]!=1:
    k=min(k,a[i+1]-a[i]-1)
    b.append(a[i+1]-a[i]-1)
for i in b:
  ans+=int((i+k-0.1)//k)
print(ans)