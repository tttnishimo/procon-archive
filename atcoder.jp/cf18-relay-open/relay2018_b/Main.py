import itertools
S=input()
g=list(map(int,input().split()))
A=[[1,0],[-1,0],[0,1],[0,-1]]
for i in itertools.permutations(A,4):
  now=[0,0]
  for j in S:
    if j=='W':
      now=[now[k]+i[0][k] for k in range(2)]
    elif j=='X':
      now=[now[k]+i[1][k] for k in range(2)]
    elif j=='Y':
      now=[now[k]+i[2][k] for k in range(2)]
    else:
      now=[now[k]+i[3][k] for k in range(2)]
    if now==g:
      print('Yes')
      exit()
if g==[0,0]:
  print('Yes')
  exit()
print('No')