n=int(input())
a=list(map(int,input().split()))
b=[[n,0] for _ in range(60)]
ans=0
for i in range(60):
  b=sum([j>>i&1 for j in a])
  ans+=pow(2,i,10**9+7)*b*(n-b)
  ans%=10**9+7
print(ans)