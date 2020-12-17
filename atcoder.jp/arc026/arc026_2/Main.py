n=int(input())
flg=0
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    if n//i==i:
      flg+=i
    else:
      flg+=i+n//i
if flg==2*n:
  print('Perfect')
elif flg>2*n:
  print('Abundant')
else:
  print('Deficient')