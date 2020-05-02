n = int(input())
a,b = map(int, input().split())
flg = 0
for i in range(10000):
  if n * i >= a and n * i <= b:
    flg = 1
if flg == 1:
  print('OK')
else:
  print('NG')