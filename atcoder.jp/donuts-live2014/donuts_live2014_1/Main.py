n=int(input())
if n%2==1:
  print('error')
else:
  a=list(map(int,input().split()))
  print(sum(a[1::2])-sum(a[::2]))