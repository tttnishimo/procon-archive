n = int(input())
k = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
  res += 2 * min(abs(a[i] - k), a[i])
print(res)