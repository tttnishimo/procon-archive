n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
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
  else:
    par[y]=x
    a[x]+=a[y]
    b[x]+=b[y]
for i in range(m):
  p,q=map(int,input().split())
  unite(p-1,q-1)
flg=0
for i in range(n):
  if a[find(i)]!=b[find(i)]:
    flg=1
if flg==0:
  print('Yes')
else:
  print('No')