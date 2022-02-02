from collections import deque
a,N=map(int,input().split())
M=10**(len(str(N)))
seen=[-1]*M
seen[1]=0
Q=deque()
Q.append(1)
while len(Q):
  q=Q.popleft()
  if q*a<M and seen[q*a]==-1:
    seen[q*a]=seen[q]+1
    Q.append(q*a)
  if q>=10 and q%10!=0:
    q2=int(str(q)[-1]+str(q)[:-1])
    if q2<M and seen[q2]==-1:
      seen[q2]=seen[q]+1
      Q.append(q2)
print(seen[N])