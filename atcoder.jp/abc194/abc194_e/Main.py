N,M=map(int,input().split())
A=list(map(int,input().split()))
L=[0]*(max(A)+2)
for i in A[:M]:
  L[i]+=1
mex=L.index(0)
for i in range(N-M):
  L[A[i]]-=1
  L[A[i+M]]+=1
  if L[A[i]]==0:
    mex=min(mex,A[i])
print(mex)