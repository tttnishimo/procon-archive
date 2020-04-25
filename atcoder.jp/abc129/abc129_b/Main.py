n = int(input())
a = list(map(int, input().split()))
res = 1000
for i in range(n):
  res = min(res,abs(sum(a) - 2 * sum(a[:i])))
print(res)