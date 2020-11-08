from itertools import accumulate
n=int(input())
a=list(map(int,input().split()))
c=list(accumulate(a))
c2=list(accumulate(c))
ans=max(0,a[0])
max_c=c[0]
for i in range(1,n):
  max_c=max(max_c,c[i-1])
  ans=max(ans,c2[i],c2[i-1]+max_c)
print(ans)