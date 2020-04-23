n,k = map(int, input().split())
res = 0
tmp = 0
for i in range(n):
  tmp += int(input())
  if res == 0 and tmp >= k:
    res = i + 1
print(res)
