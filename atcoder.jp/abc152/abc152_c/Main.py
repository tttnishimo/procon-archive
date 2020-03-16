n = int(input())
a = list(map(int, input().split()))
tmp = a[0]
res = 0
for i in range(n):
  if tmp >= a[i]:
    tmp = a[i]
    res += 1
print(res)