n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in range(n):
  if i == 0 and a[i] >= b[i]:
    res += b[i]
    b[i] = 0
  elif i == 0 and a[i] < b[i]:
    res += a[i]
    b[i] -= a[i]
  elif a[i] >= b[i] + b[i-1]:
    res += b[i] + b[i-1]
    b[i] = 0
  else:
    res += a[i]
    if b[i-1] >= a[i]:
      pass
    else:
      b[i] -= a[i] - b[i-1]
if a[-1] >= b[-1]:
  res += b[-1]
else:
  res += a[-1]
print(res)