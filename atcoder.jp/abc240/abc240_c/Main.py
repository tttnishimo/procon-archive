N,X=map(int,input().split())
l=[0]*(X+1)
l[0]=1
for i in range(N):
  a,b=map(int,input().split())
  t=[0]*(X+1)
  for j in range(X):
    if l[j]==1:
      if j+a<=X:
        t[j+a]=1
      if j+b<=X:
        t[j+b]=1
  l=list(t)
if l[-1]:
  print('Yes')
else:
  print('No')