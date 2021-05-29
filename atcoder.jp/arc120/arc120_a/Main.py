import itertools
N=int(input())
A=list(map(int,input().split()))
B=list(itertools.accumulate(A))
ans=A[0]
max_A=A[0]
print(ans+max_A)
for i in range(1,N):
  max_A=max(max_A,A[i])
  ans+=B[i]
  print(ans+(i+1)*max_A)