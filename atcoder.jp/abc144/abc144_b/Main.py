n = int(input())
flg = 0
for i in range(1,10):
  for j in range(1,10):
    if i * j == n:
      flg = 1
      break
if flg == 1:
  print('Yes')
else:
  print('No')