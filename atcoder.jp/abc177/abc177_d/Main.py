n,m=map(int,input().split())
par=[i for i in range(n+1)]
size=[1]*(n+1)
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
  if size[x]<size[y]:
    size[y]+=size[x]
    par[x]=y
  else:
    size[x]+=size[y]
    par[y]=x
for i in range(m):
  a,b=map(int,input().split())
  unite(a,b)
print(max(size))