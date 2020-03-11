n = int(input())
a = list(map(int, input().split()))
res1 = []
res2 = []
if n % 2 == 1:
  res1.append(a.pop(-1))
  n = n -1
  for i in range(n//2):
    res1.append(a[n-2-2*i])
    res2.append(a[1+i*2])
  res1.extend(res2)
  print(*res1)
else:
  for i in range(n//2):
    res1.append(a[n-1-2*i])
    res2.append(a[i*2])
  res1.extend(res2)
  print(*res1)