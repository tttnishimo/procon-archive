n = int(input())
li = list(map(int, input().split()))
res = -1
for i in range(101):
  sum = 0
  if i == 0:
    pass
  else:
    for j in range(n):
      sum = sum + (li[j]-i)**2
    if res == -1:
      res = sum
    elif res > sum:
      res = sum
print(res)