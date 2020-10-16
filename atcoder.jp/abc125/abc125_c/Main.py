import math
n=int(input())
a=list(map(int,input().split()))
b=[a[-i-1] for i in range(n)]
l,r=[0],[0]
ans=0
for i in range(n):
  l.append(math.gcd(l[-1],a[i]))
  r.append(math.gcd(r[-1],b[i]))
for i in range(n):
  ans=max(math.gcd(l[i],r[n-1-i]),ans)
print(ans)