import bisect
N,K=map(int,input().split())
A=list(map(int,input().split()))
print(sum(bisect.bisect(A,A[i]+K)-i-1 for i in range(N-1)))