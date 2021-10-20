X,Y=map(int,input().split())
x,y=0,0
for i in range(1,max(X,Y)+1):
  if X%i==0:
    x+=1
  if Y%i==0:
    y+=1
if x>y:
  print('X')
elif x<y:
  print('Y')
else:
  print('Z')