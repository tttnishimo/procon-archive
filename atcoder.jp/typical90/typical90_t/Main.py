a,b,c=map(int,input().split())
if a==1 and c==1:
  print('No')
elif a==1:
  print('Yes')
elif a<c**b:
  print('Yes')
else:
  print('No')