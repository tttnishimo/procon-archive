n = int(input())
flg = 0
for i in range(26):
  for j in range(16):
    if 4 * i + 7 * j == n:
      flg = 1
if flg == 1:
  print('Yes')
else:
  print('No')