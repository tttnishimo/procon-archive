m,n=map(int,input().split())
if m%n==0:
  print(m//n)
else:
  print(m-m//n*(n-1))