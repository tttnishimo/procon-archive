N,M=map(int,input().split())
A=[[] for _ in range(N+1)]
for i in range(M):
  a=list(map(int,input().split()))
  for j in range(1,a[0]):
    for k in range(j+1,a[0]+1):
      A[a[j]].append(a[k])
      A[a[k]].append(a[j])
for i in range(1,N+1):
  if len(set(A[i]))!=N-1:
    print('No')
    exit()
print('Yes')