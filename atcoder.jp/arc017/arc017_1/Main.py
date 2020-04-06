n = int(input())
flg = 0
for i in range(2,int(pow(n,1/2)+1)):
  if n % i == 0:
    flg = 1
if flg == 0:
  print('YES')
else:
  print('NO')