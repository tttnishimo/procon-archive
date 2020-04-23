n = int(input())
a = list(map(int, input().split()))
res = n
tmp = 1
for i in range(n):
  if a[i] == tmp:
    res -= 1
    tmp += 1
if tmp == 1:
  print(-1)
elif res == n:
  print(0)
else:
  print(res)
