V,A,B,C=map(int,input().split())
if V>=A+B+C:
  V-=(A+B+C)*(V//(A+B+C))
V-=A
if V<0:
  print('F')
  exit()
V-=B
if V<0:
  print('M')
else:
  print('T')