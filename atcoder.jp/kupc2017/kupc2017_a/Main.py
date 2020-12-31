n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
if sum(a)<k:
  print(-1)
else:
  for i in range(n+1):
    if sum(a[:i])>=k:
      print(i)
      break