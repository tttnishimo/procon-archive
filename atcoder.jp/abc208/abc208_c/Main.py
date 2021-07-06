N,K=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(A)
if K%N==0:
  print(*[K//N]*N,sep='\n')
else:
  print(*[K//N+1 if A[i]<B[K%N] else K//N for i in range(N)],sep='\n')