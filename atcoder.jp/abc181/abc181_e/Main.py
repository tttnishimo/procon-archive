import bisect
n,m=map(int,input().split())
h=list(map(int,input().split()))
w=list(map(int,input().split()))
h.sort()
w.sort()
a=[h[2*i+1]-h[2*i] for i in range(n//2)]+[-1]
b=[-1]+[h[2*i+2]-h[2*i+1] for i in range(n//2)]
ans=10000000000000
c=[sum(b[1:])]
for i in range(n//2):
  c.append(c[-1]+a[i]-b[i+1])
for i in range(m):
  d=(bisect.bisect_left(h,w[i]))//2
  ans=min(ans,c[d]+abs(h[d*2]-w[i]))
print(ans)