n,m,q=map(int,input().split())
ans=[[] for _ in range(m+1)]
for i in range(q):
  a=list(map(int,input().split()))
  if a[0]==2:
    ans[a[2]].append(a[1])
  else:
    tmp=0
    for j in ans:
      if a[1] in j:
        tmp+=n-len(j)
    print(tmp)