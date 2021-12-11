import numpy as np
N=int(input())
A=list(map(int,np.base_repr(N,3)))
for i in range(len(A)-1):
  if A[-i-1]==2:
    A[-i-2]+=1
    A[-i-1]=-1
  elif A[-i-1]==3:
    A[-i-2]+=1
    A[-i-1]=0
if A[0]==2:
  A[0]=-1
  A.insert(0,1)
elif A[0]==3:
  A[0]=0
  A.insert(0,1)
ans=[]
for i in range(len(A)):
  if A[i]==1:
    ans.append(3**(len(A)-i-1))
  elif A[i]==-1:
    ans.append(-3**(len(A)-i-1))
print(len(ans))
print(*ans)