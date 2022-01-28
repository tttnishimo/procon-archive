import collections
N,K=map(int,input().split())
A=collections.Counter(input() for _ in range(N))
B=[[10**10,''],[0,'']]
for i in A:
  B.append([A[i],i])
B.sort(reverse=True)
if B[K][0]!=B[K-1][0] and B[K][0]!=B[K+1][0]:
  print(B[K][1])
else:
  print('AMBIGUOUS')