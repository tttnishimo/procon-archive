import collections
n=int(input())
a=dict(collections.Counter(list(map(int,input().split()))))
q=int(input())
ans=0
for i in a:
  ans+=i*a[i]
for i in range(q):
  b,c=map(int,input().split())
  ans+=a.get(b,0)*(c-b)
  print(ans)
  a[c]=a.get(b,0)+a.get(c,0)
  a[b]=0