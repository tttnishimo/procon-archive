n=int(input())
b=1
flg=0
while 5**b<=n:
  m=n-5**b
  a=1
  while 3**a<=m:
    if 3**a==m:
      print(a,b)
      flg=1
      break
    a+=1
  b+=1
if flg==0:
  print(-1)