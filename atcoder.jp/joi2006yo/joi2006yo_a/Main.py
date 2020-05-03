n = int(input())
res = [0,0]
for i in range(n):
  a,b = map(int, input().split())
  if a > b:
    res[0] += a + b
  elif a < b:
    res[1] += a + b
  else:
    res[0] += a
    res[1] += b
print(*res)