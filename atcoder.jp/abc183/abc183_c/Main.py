from itertools import permutations
n,k=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
c=list(permutations(range(1,n),n-1))
ans=0
for i in c:
  t=0
  d=0
  for j in i:
    d+=a[t][j]
    t=j
  d+=a[t][0]
  if d==k:
    ans+=1
print(ans)