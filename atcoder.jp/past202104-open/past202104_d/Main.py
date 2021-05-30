import itertools
N,K=map(int,input().split())
A=list(map(int,input().split()))
B=[0]+list(itertools.accumulate(A))
for i in range(K,N+1):
  print(B[i]-B[i-K])