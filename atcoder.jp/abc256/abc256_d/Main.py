import itertools
N=int(input())
A=[0]*(2*10**5+1)
for i in range(N):
  L,R=map(int,input().split())
  A[L]+=1
  A[R]+=-1
A=list(itertools.accumulate(A))
for i in range(2*10**5):
  if A[i]==0 and A[i+1]>0:
    ans=i+1
  elif A[i]>0 and A[i+1]==0:
    print(ans,i+1)