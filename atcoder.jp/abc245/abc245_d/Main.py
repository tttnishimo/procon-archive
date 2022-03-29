N,M=map(int,input().split())
A=list(map(int,input().split()))
C=list(map(int,input().split()))
A.reverse()
C.reverse()
B=[]
for i in range(M+1):
  t=C[i]//A[0]
  B.append(t)
  for j in range(N+1):
    C[i+j]-=t*A[j]
print(*reversed(B))