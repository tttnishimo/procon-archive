x,k,d=map(int,input().split())
if k*d>abs(x):
  x-=(x//(2*d))*2*d
  if k%2==0:
    print(min(abs(x-2*d),x,abs(x+2*d)))
  else:
    print(min(abs(x-d),abs(x+d)))
elif k*d==abs(x):
  print(0)
else:
  print(abs(x)-k*d)