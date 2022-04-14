from collections import deque
d=deque()
for i in range(int(input())):
  q=list(map(int,input().split()))
  if q[0]==1:
    d.append([q[1],q[2]])
  else:
    ans=0
    t=d[0]
    while q[1]>t[1]:
      ans+=t[0]*t[1]
      q[1]-=t[1]
      d.popleft()
      t=d[0]
    ans+=d[0][0]*q[1]
    print(ans)
    if len(d)>0:
      d[0][1]-=q[1]
    ans=0