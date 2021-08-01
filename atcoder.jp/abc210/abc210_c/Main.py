N,K=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in a[:K]:
  if d.get(i,0)==0:
    d[i]=1
  else:
    d[i]+=1
ans=len(d)
for i in range(K,N):
  if d.get(a[i],0)==0:
    d[a[i]]=1
  else:
    d[a[i]]+=1
  d[a[i-K]]-=1
  if d[a[i-K]]==0:
    d.pop(a[i-K])
  ans=max(ans,len(d))
print(ans)