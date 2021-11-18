N,K=map(int,input().split())
c=list(map(int,input().split()))
p=list(map(int,input().split()))
if len(set(c))<K:
  print(-1)
else:
  d={}
  for i in range(N):
    d[c[i]]=min(d.get(c[i],10**9),p[i])
  A=list(d.values())
  A.sort()
  print(sum(A[:K]))