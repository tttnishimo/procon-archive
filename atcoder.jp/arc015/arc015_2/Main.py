n = int(input())
res = [0,0,0,0,0,0]
for i in range(n):
  h,l = map(float, input().split())
  if h >= 35.0:
    res[0] += 1
  elif h >= 30.0:
    res[1] += 1
  elif h >= 25.0:
    res[2] += 1
  if l >= 25.0:
    res[3] += 1
  if l < 0.0 and h >= 0.0:
    res[4] += 1
  if h < 0.0:
    res[5] += 1
print(*res)
