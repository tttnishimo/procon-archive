n,m=map(int,input().split())
ans=0
for i in range(n):
  ans=max(ans,sum(list(map(int,input().split()))))
print(ans)