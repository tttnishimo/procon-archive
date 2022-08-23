N,M,T=map(int,input().split())
A=list(map(int,input().split()))
for i in range(M):
  X,Y=map(int,input().split())
  A[X-1]-=Y
for a in A:
  T-=a
  if T<1:
    print('No')
    exit()
print('Yes')