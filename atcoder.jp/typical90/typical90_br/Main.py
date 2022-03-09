N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
a=sorted(i for i,j in A)[N//2]
b=sorted(j for i,j in A)[N//2]
ans=0
for i,j in A:
  ans+=abs(i-a)+abs(j-b)
print(ans)