n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n//2):
  ans+=abs(a[-i-1]-a[i])*(n-2*i-1)
print(ans)