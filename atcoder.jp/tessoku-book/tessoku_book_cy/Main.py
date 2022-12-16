N=int(input())
A=[True]*(N+1)
for i in range(2,int(N**.5)+1):
  for j in range(i*2,N+1,i):
    A[j]=False
for i in range(2,N+1):
  if A[i]:
    print(i)