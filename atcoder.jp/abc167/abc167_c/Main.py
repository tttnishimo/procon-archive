import itertools
n,m,x = map(int, input().split())
a = []
res = 10000000
for i in range(n):
  a.append(list(map(int, input().split())))
for i in range(1,n+1):
  l = itertools.combinations(range(n),i)
  for j in l:
    tmp = [0]*(m+1)
    for k in j:
      for o in range(m+1):
        tmp[o] += a[k][o]
    flg = 0
    for o in range(1,m+1):
      if tmp[o] < x:
        flg = 1
    if flg == 0:
      res = min(res, tmp[0])
if res == 10000000:
  print(-1)
else:
  print(res)
