import math
n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
h=[]
w=[]
par=[-1]*n
def find(x):
  if par[x]<0:
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
    if par[x]>par[y]:
      x,y=y,x
    par[x]+=par[y]
    par[y]=x
def size(x):
  return -par[find(x)]
for i in range(n-1):
  for j in range(i+1,n):
    flg_h=0
    flg_w=0
    for l in range(n):
      if a[i][l]+a[j][l]>k:
        flg_w=1
      if a[l][i]+a[l][j]>k:
        flg_h=1
    if flg_w==0:
      w.append([i,j])
    if flg_h==0:
      h.append([i,j])
for i in w:
  unite(i[0],i[1])
ans=1
tmp=[]
for i in range(n):
  if find(i) not in tmp:
    ans*=math.factorial(size(i))
    ans%=998244353
    tmp.append(find(i))
par=[-1]*n
for i in h:
  unite(i[0],i[1])
tmp=[]
for i in range(n):
  if find(i) not in tmp:
    ans*=math.factorial(size(i))
    ans%=998244353
    tmp.append(find(i))
print(ans)