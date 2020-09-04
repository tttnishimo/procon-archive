t=int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
if n<m:
  print('no')
else:
  j=0
  flg=0
  for i in range(m):
    while True:
      if j>=n:
        flg=1
        break
      elif a[j]<=b[i]<=a[j]+t:
        break
      j+=1
    j+=1
  if flg==1:
    print('no')
  elif j>=n:
    if a[-1]<=b[-1]<=a[-1]+t:
      print('yes')
    else:
      print('no')
  else:
    print('yes')