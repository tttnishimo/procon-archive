N,D=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
A.sort(key=lambda x:x[1])
r=A[0][1]+D-1
ans=1
for i in A:
  if r<i[0]:
    r=i[1]+D-1
    ans+=1
print(ans)