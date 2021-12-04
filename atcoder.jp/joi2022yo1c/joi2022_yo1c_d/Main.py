N,M=map(int,input().split())
A=[i+1 for i in range(N)]
for i in range(M):
  X,Y=map(int,input().split())
  A[X-1]=Y
print(*A,sep='\n')