X,A,B,C=map(int,input().split())
a=X/A+C
b=X/B
if a==b:
  print('Tie')
elif a>b:
  print('Tortoise')
else:
  print('Hare')