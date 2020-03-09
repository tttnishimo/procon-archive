a = list(map(int, input().split()))
r = []
for i in range(3):
  for j in range(1, 4 - i):
    for k in range(1, 5 - i - j):
      tmp = a[i] + a[i + j] + a[i + j + k]
      if tmp in r:
        pass
      else:
        r.append(tmp)
r.sort()
print(r[-3])