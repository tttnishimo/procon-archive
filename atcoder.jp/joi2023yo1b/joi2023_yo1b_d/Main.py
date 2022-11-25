N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=set(map(int,input().split()))
ans=0
for i in range(N):
  ans+=A[i]
  if ans in B:
    ans=0
print(ans)