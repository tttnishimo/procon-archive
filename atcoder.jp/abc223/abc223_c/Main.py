N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
t=sum(i/j for i,j in A)/2
ans=0
for i,j in A:
  if t>i/j:
    ans+=i
    t-=i/j
  else:
    print(ans+t*j)
    exit()