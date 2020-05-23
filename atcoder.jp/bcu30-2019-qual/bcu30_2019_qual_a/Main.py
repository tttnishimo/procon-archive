n,p=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
  p -= a[i]
  if p < 0:
    ans=i
    break
  elif p == 0:
    ans=i+1
    break
if p > 0:
  print(n)
else:
  print(ans)