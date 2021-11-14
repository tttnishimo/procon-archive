N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
i,j,k=0,0,0
ans=0
while i<N:
  while j<N and A[i]>=B[j]:
    j+=1
  if j==N:
    break
  while k<N and B[j]>=C[k]:
    k+=1
  if k==N:
    break
  ans+=1
  i+=1
  j+=1
  k+=1
print(ans)