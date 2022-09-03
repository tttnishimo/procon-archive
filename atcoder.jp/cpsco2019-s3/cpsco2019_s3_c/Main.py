N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort()
l=A[0][0]
r=A[0][1]
ans=1
for i in range(N):
  if A[i][0]>r:
    ans+=1
    l=A[i][0]
    r=A[i][1]
  else:
    r=max(r,A[i][1])
print(ans)