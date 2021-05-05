import bisect
import itertools
N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
b.sort()
c.sort()
d=list(reversed([N-bisect.bisect_right(c,i) for i in b]))
d=list(reversed(list(itertools.accumulate(d))))
d.append(0)
ans=0
for i in range(N):
  ans+=d[bisect.bisect_right(b,a[i])]
print(ans)