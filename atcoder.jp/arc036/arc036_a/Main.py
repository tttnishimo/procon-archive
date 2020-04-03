n,m = map(int, input().split())
a = []
res = 100001
for i in range(n):
  a.append(int(input()))
  if i >= 2 and sum(a) < m:
    res = min(i+1,res)
  if len(a) == 3:
    a = a[1:]
if res == 100001:
  print(-1)
else:
  print(res)