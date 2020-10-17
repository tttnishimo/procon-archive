n,m=map(int,input().split())
par=[i for i in range(n+1)]
def find(x):
  if par[x]==x:
    return x
  else:
    par[x]=find(par[x])
    return par[x]
def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return 0
  par[x]=y
for i in range(m):
  p,q=map(int,input().split())
  unite(p,q)
ans=0
for i in range(1,n+1):
  if i==par[i]:
    ans+=1
print(ans-1)