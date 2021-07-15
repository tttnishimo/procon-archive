N,X=map(int,input().split())
A=sum(list(map(int,input().split())))
if X>=A-N//2:
  print('Yes')
else:
  print('No')