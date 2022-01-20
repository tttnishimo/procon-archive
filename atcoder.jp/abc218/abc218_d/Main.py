N=int(input())
S=set()
for _ in range(N):
  x,y=map(int,input().split())
  S.add(tuple([x,y]))
ans=0
for a in S:
  for b in S:
    if a[0]<b[0] and a[1]<b[1] and (a[0],b[1]) in S and (b[0],a[1]) in S:
      ans+=1
print(ans)