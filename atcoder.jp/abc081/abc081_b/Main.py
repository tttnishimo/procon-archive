n = int(input())
a = list(map(int, input().split()))
res = 40
for i in range(n):
  tmp = 0
  while a[i] % 2 == 0:
    a[i] = a[i] // 2
    tmp += 1
  res = min(res, tmp)
print(res)