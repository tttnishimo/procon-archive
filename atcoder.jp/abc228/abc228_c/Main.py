N,K=map(int,input().split())
A=[sum(map(int,input().split())) for _ in range(N)]
B=list(A)
B.sort()
C=B[-K]
for i in A:
  if i+300<C:
    print('No')
  else:
    print('Yes')