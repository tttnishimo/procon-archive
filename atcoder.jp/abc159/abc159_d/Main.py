import collections
n = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
tmp = {}
sum = 0
for j in c:
  tmp[j] = c[j] * (c[j] - 1) // 2
  sum += c[j] * (c[j] - 1) // 2
for i in range(n):
  print((c[a[i]] - 1) * (c[a[i]] - 2) // 2 + sum - tmp[a[i]])