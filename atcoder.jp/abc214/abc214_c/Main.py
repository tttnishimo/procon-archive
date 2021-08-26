N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
A=[T[0]]
for i in range(N-1):
  A.append(min(A[-1]+S[i],T[i+1]))
for i in range(N):
  A[i]=min(A[i-1]+S[i-1],A[i])
for i in range(N):
  print(min(A[i],T[i]))