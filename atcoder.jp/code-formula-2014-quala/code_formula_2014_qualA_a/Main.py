n=int(input())
flg = 0
for i in range(101):
  if i**3 == n:
    flg = 1
if flg == 1:
  print('YES')
else:
  print('NO')