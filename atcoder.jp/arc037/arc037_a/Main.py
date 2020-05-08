n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n):
  res += max(0, 80 - a[i])
print(res)