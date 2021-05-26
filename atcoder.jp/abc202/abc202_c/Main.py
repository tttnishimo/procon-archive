import collections
N=int(input())
A=collections.Counter(list(map(int,input().split())))
B=list(map(int,input().split()))
C=collections.Counter(list(map(int,input().split())))
ans=0
for i in range(N):
  ans+=A[B[i]]*C[i+1]
print(ans)