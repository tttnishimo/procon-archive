n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
l,r=0,0
ans=0
t=a[0]
while True:
  if t<=k:
    ans=max(ans,r-l+1)
    r+=1
    if r<n:
      t*=a[r]
  else:
    t//=max(a[l],1)
    l+=1
    if r<l:
      r+=1
      if r<n:
        t*=a[r]
  if r>=n:
    break
if a.count(0)>0:
  print(n)
else:
  print(ans)