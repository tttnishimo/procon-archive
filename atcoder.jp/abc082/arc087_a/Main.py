import collections
n=int(input())
a=list(map(int,input().split()))
c=collections.Counter(a)
ans=0
for i in c:
  if i < c[i]:
    ans+=c[i]-i
  elif i > c[i]:
    ans+=c[i]
print(ans)