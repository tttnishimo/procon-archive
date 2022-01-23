N=int(input())
A=list(map(int,input().split()))
a=A[-1]
for i in range(1,N):
  if A[i-1]>A[i]:
    a=A[i-1]
    break
print(*[i for i in A if i!=a])