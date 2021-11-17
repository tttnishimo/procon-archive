N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=0
for i in range(N-2):
  a=A[i][0]
  b=A[i][1]
  for j in range(i+1,N-1):
    c=A[j][0]
    d=A[j][1]
    for k in range(j+1,N):
      if (c-a)*(A[k][1]-b)!=(A[k][0]-a)*(d-b):
        ans+=1
print(ans)