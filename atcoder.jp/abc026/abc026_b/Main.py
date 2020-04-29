import math
n = int(input())
a = []
res = 0
for i in range(n):
  a.append(int(input()))
a = sorted(a,reverse=True)
for i in range(n):
  if i == 0:
    res += a[i] * a[i] * math.pi
  elif i % 2 == 1:
    res -= (a[i] * a[i]) * math.pi
  elif i % 2 == 0:
    res += (a[i] * a[i]) * math.pi
print(res)