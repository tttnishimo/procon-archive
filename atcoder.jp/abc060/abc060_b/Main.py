a,b,c = map(int, input().split())
flg = 0
for i in range(1,101):
  tmp = a * i % b
  if tmp == c:
    flg = 1
if flg == 1:
  print('YES')
else:
  print('NO')