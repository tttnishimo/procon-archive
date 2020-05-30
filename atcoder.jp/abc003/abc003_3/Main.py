n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in reversed(range(k)):
  ans = (ans+a[-i-1])/2
print(ans)