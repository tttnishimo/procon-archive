a,b = map(int, input().split())
c = sum(list(map(int, input().split())))
if c > a:
  print(-1)
else:
  print(a-c)