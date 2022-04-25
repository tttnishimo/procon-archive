A,B,C,D,E,F,X=map(int,input().split())
a=X//(A+C)*B*A+min(A*B,(X-X//(A+C)*(A+C))*B)
b=X//(D+F)*E*D+min(D*E,(X-X//(D+F)*(D+F))*E)
if a>b:
  print('Takahashi')
elif a==b:
  print('Draw')
else:
  print('Aoki')