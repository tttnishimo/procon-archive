n,t,e=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(t-e,t+e+1):
  for j in range(n):
    if i % a[j] == 0:
      ans = j+1
      break
if ans == 0:
  print(-1)
else:
  print(ans)