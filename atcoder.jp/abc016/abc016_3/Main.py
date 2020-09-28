n,m=map(int,input().split())
a=[[] for _ in range(n+1)]
for i in range(m):
  p,q=map(int,input().split())
  a[p].append(q)
  a[q].append(p)
for i in range(1,n+1):
  ans=[]
  for j in a[i]:
    for k in range(1,n+1):
      if (j in a[k]) and k!=i and (k not in a[i]) and (k not in ans):
        ans.append(k)
  print(len(ans))