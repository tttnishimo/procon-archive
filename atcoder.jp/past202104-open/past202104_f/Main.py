N,L,T,X=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
i=0
t=0
ans=0
while i<N:
  if A[i][1]>=L:
    t+=A[i][0]
  else:
    t=0
  if t>T:
    ans+=X+T-t+A[i][0]
    t=0
    if A[i][1]>=L and A[i][0]>T:
      print('forever')
      exit()
    continue
  elif t==T:
    t=0
    ans+=X
  ans+=A[i][0]
  i+=1
if t==T:
  ans+=X
print(ans)