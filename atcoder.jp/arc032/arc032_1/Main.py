n = int(input())
m = n * (n + 1) //2
flg = 0
for i in range(2,n+1):
  if m % i == 0:
    flg = 1
if n == 1:
  flg = 1
if flg == 0:
  print('WANWAN')
else:
  print('BOWWOW')