input()
A=list(map(int,input().split()))
ans=0
d={}
for a in A:
  d[a]=d.get(a,0)+1
for a in A:
  if d.get(100000-a):
    if a==50000:
      ans+=d[50000]*(d[50000]-1)//2
      d[a]=0
    else:
      ans+=d[100000-a]
      d[a]=0
print(ans)