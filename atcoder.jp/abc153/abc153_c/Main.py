n,k = map(int, input().split())
a = sorted(list(map(int, input().split())))
res = 0
if k >= n:
  print(0)
else:
  a = a[:n-k]
  for i in a:
    res += i
  print(res)