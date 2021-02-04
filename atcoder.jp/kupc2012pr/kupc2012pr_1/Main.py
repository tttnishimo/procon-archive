m,n=map(int,input().split())
if m<2:
  print(m+n+1)
elif m<3:
  print(2*(n+3)-3)
else:
  print(2**(n+3)-3)