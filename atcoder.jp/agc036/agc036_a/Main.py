s=int(input())
if s==10**18:
  print(0,0,1000000000,0,0,1000000000)
else:
  a=int(s**0.5)+1
  print(0,0,a,a*a-s,1,a)