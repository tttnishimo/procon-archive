N,M=map(int,input().split())
ans=[[] for _ in range(N+1)]
for _ in range(M):
  A,B=map(int,input().split())
  ans[A].append(B)
  ans[B].append(A)
ans=ans[1:]
for i in ans:
  i.sort()
  print(len(i),*i)