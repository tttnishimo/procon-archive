N=int(input())
C=list(map(int,input().split()))
s=sum(C)
t=[0,0]
mi=[min(C),min(C[::2])]
for _ in range(int(input())):
  q=list(map(int,input().split()))
  if q[0]==1:
    if C[q[1]-1]-t[q[1]%2]>=q[2]:
      C[q[1]-1]-=q[2]
      mi[0]=min(mi[0],C[q[1]-1])
      if q[1]%2:
        mi[1]=min(mi[1],C[q[1]-1])
  elif q[0]==2:
    if mi[1]-t[1]>=q[1]:
      t[1]+=q[1]
  else:
    if mi[0]-t[0]>=q[1] and mi[1]-t[1]>=q[1]:
      t[0]+=q[1]
      t[1]+=q[1]
print(s-sum(C)+t[0]*(N//2)+t[1]*(-(-N//2)))