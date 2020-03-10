n,k,s = map(int, input().split())
res = [s]*k
if s > 100:
  for i in range(n - k):
    res.append(13)
  print(*res)
else:
  for i in range(n - k):
    res.append(209)
  print(*res)