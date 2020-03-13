n,m = map(int, input().split())
a = []
for i in range(n):
  a.append(int(input()))
a.sort()

tmp = 1000000000
for i in range(n - m + 1):
  tmp = min(tmp, a[i + m - 1] - a[i])
print(tmp)