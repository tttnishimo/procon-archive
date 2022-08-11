import heapq
A=[]
B=[]
d={}
for _ in range(int(input())):
  q=list(map(int,input().split()))
  if q[0]==1:
    if d.get(q[1],0):
      d[q[1]]+=1
    else:
      d[q[1]]=1
      heapq.heappush(A,q[1])
      heapq.heappush(B,-q[1])
  elif q[0]==2:
    if d.get(q[1],0):
      d[q[1]]=max(0,d[q[1]]-q[2])
  else:
    while d[A[0]]==0:
      heapq.heappop(A)
    while d[-B[0]]==0:
      heapq.heappop(B)
    print(-B[0]-A[0])