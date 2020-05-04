n,t = map(int, input().split())
res = 1001
for i in range(n):
  a,b = map(int, input().split())
  if b <= t:
    res = min(res, a)
if res == 1001:
  print('TLE')
else:
  print(res)