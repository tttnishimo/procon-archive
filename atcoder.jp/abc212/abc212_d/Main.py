import heapq
q=int(input())
h=[]
sum=0
for i in range(q):
  l=list(map(int,input().split()))
  if l[0]==1:
    heapq.heappush(h,l[1]-sum)
  elif l[0]==2:
    sum+=l[1]
  elif l[0]==3:
    print(heapq.heappop(h)+sum)