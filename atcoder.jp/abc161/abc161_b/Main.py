n,m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(n):
  if a[i] >= sum(a)/(4*m):
    res += 1
if res >= m:
  print('Yes')
else:
  print('No')