n,x = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(n):
  if a[i] + x >= max(a):
    res += 1
print(res)