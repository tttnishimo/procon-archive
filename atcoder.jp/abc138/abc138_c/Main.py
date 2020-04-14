n = int(input())
a = sorted(list(map(int, input().split())))
res = a[0]
for i in range(n-1):
  res = (res + a[i + 1]) / 2
print(res)