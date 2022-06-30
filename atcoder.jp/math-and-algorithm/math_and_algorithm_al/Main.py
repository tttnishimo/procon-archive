T=int(input())
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
ans=[0]*(T+1)
for l,r in A:
  ans[l]+=1
  ans[r]-=1
for i in range(1,T):
  ans[i]+=ans[i-1]
print(*ans[:-1],sep='\n')