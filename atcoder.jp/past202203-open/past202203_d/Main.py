T,N=map(int,input().split())
A=list(map(int,input().split()))
print(sum(A))
for i in range(T-1):
  B=list(map(int,input().split()))
  A=[max(A[i],B[i]) for i in range(N)]
  print(sum(A))