n = int(input())
res = 0
for i in range(50001):
  if int(i * 1.08) == n:
    res = i
if res != 0:
  print(res)
else:
  print(':(')