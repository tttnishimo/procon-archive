n,m,q=map(int,input().split())
gr=[[] for _ in range(n+1)]
for i in range(m):
  s,t=map(int,input().split())
  gr[s].append(t)
  gr[t].append(s)
c=list(map(int,input().split()))
c.insert(0,0)
for i in range(q):
  a=list(map(int,input().split()))
  if a[0]==1:
    print(c[a[1]])
    for j in gr[a[1]]:
      c[j]=c[a[1]]
  else:
    print(c[a[1]])
    c[a[1]]=a[2]