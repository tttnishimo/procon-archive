n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
ans=0
k=int(input())
b=[list(map(int,input().split())) for _ in range(k)]
for i in range(2**k):
  t={b[j][(i>>j)&1]:1 for j in range(k)}
  tmp=0
  for j in a:
    if t.get(j[0],0) and t.get(j[1],0):
      tmp+=1
  ans=max(ans,tmp)
print(ans)