X,Y=map(int,input().split())
if Y==0:
  print('ERROR')
else:
  n=str(float(X/Y))+'0'
  print(n[:n.index('.')+3])