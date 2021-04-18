n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=0
t=[0]
for i in range(n):
  t.append((t[-1]*2+a[i])%998244353)
for i in range(n):
  ans+=a[i]*(a[i]+t[i])
  ans%=998244353
print(ans)