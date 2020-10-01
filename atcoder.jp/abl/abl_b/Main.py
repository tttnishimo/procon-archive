a,b,c,d=map(int,input().split())
if (a<d and b<c) or (b>c and a>d):
  print('No')
else:
  print('Yes')