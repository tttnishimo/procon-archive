N=int(input())
S=[[int(i) for i in input()] for _ in range(N)]
ans=10**10
for x in range(10):
  t=set()
  for s in S:
    i=s.index(x)
    while i in t:
      i+=10
    t.add(i)
  ans=min(ans, max(t))
print(ans)