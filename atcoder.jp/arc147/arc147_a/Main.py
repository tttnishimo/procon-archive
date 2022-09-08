from collections import deque
N=int(input())
A=list(map(int,input().split()))
A.sort()
A=deque(A)
ans=0
while True:
  a=A[-1]%A[0]
  ans+=1
  if a==1:
    print(ans+len(A)-1)
    exit()
  elif a==0:
    A.pop()
  else:
    A.pop()
    A.appendleft(a)
  if len(A)==0:
    print(ans)
    exit()