N,M=map(int,input().split())
a=[{i} for i in range(N)]
for _ in range(M):
  x,y=map(int,input().split())
  a[x-1].add(y-1)
  a[y-1].add(x-1)
ans=0
for i in range(2**N):
  b=set()
  t=0
  for j in range(N):
    if (i>>j)&1:
      b.add(j)
  for j in b:
    if b<=a[j]:
      t+=1
    else:
      break
    ans=max(ans,t)
print(ans)