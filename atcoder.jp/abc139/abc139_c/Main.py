n = int(input())
a = list(map(int, input().split()))
tmp = 0
res = 0
for i in range(n-1):
  if a[i + 1] <= a[i]:
    tmp += 1
  else:
    tmp = 0
  res = max(res,tmp)
print(res)
