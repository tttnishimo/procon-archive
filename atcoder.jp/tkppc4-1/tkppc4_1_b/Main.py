n,k = map(int, input().split())
a = list(map(int, input().split()))
res = -1
for i in range(n):
  if a[i] < k:
    res = max(res,a[i])
if res == -1:
  print(-1)
else:
  print(a.index(res)+1)