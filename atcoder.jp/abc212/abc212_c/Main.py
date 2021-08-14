N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
ans=abs(A[0]-B[0])
i,j=0,0
while i<N-1 or j<M-1:
  ans=min(ans,abs(A[i]-B[j]))
  if A[i]>B[j]:
    j+=1
    if j==M:
      j-=1
      i+=1
  elif A[i]<B[j]:
    i+=1
    if i==N:
      i-=1
      j+=1
  else:
    i+=1
    j+=1
print(ans)