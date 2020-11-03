n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=[list(map(int,input().split())) for _ in range(m)]
b.sort(key=lambda x:x[1],reverse=True)
c=[]
for i in b:
  if len(c)<=n:
    for _ in range(i[0]):
      c.append(i[1])
      if len(c)>n:
        break
a.extend(c)
a.sort(reverse=True)
print(sum(a[:n]))