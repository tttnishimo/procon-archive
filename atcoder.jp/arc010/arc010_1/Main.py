n,m,a,b = map(int, input().split())
flg = 0
for i in range(m):
  if n <= a:
    n += b
  n -= int(input())
  if n < 0 and flg == 0:
    flg = i + 1
if flg == 0:
  print('complete')
else:
  print(flg)