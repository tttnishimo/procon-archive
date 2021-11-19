N,M=map(int,input().split())
A=[[input(),-i-1,0] for i in range(2*N)]
win=['GC','CP','PG']
for i in range(M):
  for j in range(N):
    if A[2*j][0][i]+A[2*j+1][0][i] in win:
      A[2*j][2]+=1
    elif A[2*j+1][0][i]+A[2*j][0][i] in win:
      A[2*j+1][2]+=1
  A.sort(key=lambda x:(x[2], x[1]),reverse=True)
for i in A:
  print(-i[1])