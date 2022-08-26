N,X,Y=map(int,input().split())
X=abs(X)
Y=abs(Y)
if N>=X+Y and N%2==(X+Y)%2:
  print('Yes')
else:
  print('No')