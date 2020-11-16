n=int(input())
a=[int(input()) for _ in range(n)]
flg=0
for i in a:
  if i%2==1:
    flg=1
if flg==1:
  print('first')
else:
  print('second')