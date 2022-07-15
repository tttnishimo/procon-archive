import math
a,b,c=map(int,input().split())
if a<2 or c<2:
  if math.log2(a)<b*math.log2(c):
    print('Yes')
  else:
    print('No')
else:
  C=c
  for i in range(b-1):
    c*=C
    if a<c:
      print('Yes')
      exit()
  if a<c:
    print('Yes')
    exit()
  print('No')