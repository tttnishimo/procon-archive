from itertools import product
n,k=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
ans=[]
for i in product(*a):
  tmp=0
  for j in i:
    tmp^=j
  ans.append(tmp)
if 0 in ans:
  print('Found')
else:
  print('Nothing')