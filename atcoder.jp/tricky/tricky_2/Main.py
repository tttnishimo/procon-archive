import sys
input=sys.stdin.readline
from decimal import*
for _ in range(int(input())):
  a,b,c=map(Decimal,input().split())
  d=b*b-4*a*c
  if a==b==c==0:
    print(3)
  elif a==b==0:
    print(0)
  elif a==0:
    print(1,-c/b)
  elif d>0:
    e,f=(-b-d.sqrt())/2/a,(-b+d.sqrt())/2/a
    print(2,min(e,f),max(e,f))
  elif d==0:
    print(1,-b/2/a)
  else:
    print(0)