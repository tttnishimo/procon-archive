n = int(input())
res = 0
for i in range(1,33):
  for j in range(2,11):
    tmp = pow(i, j)
    if tmp <= n:
      res = max(res, tmp)
print(res)