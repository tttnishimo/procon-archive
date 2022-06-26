N=int(input())
A=list(map(int,input().split()))
ans=max(0,N-4)
for _ in range(4):
  if A[-1]>3:
    ans+=1
  N-=1
  if N==0:
    break
  else:
    A[-2]+=A[-1]
  A.pop(-1)
print(ans)