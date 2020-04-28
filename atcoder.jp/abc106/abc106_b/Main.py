n = int(input())
res = 0
for i in range(2,n + 1):
  tmp = 2
  for j in range(2,i):
    if i % j == 0:
      tmp += 1
  if i % 2 == 1 and tmp == 8:
    res += 1
print(res)