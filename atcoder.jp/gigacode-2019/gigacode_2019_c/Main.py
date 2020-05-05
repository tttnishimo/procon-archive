n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = pow(10,11)
for i in range(n):
  if i == 0:
    if a[0] >= b[0]:
      res = b[0]
  else:
    a[i] += a[i-1]
    if a[i] >= b[i]:
      res = min(res, b[i])
if res == pow(10,11):
  print(-1)
else:
  print(res)
