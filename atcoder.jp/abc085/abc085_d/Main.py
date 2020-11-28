n,h=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
b=[a[i][0] for i in range(n)]
c=max(b)
d=[a[i][1] for i in range(n) if a[i][1]>c]
d.sort()
ans=0
while h>0 and d:
  h-=d.pop()
  ans+=1
if h>0:
  ans+=int((h+c-0.1)//c)
print(ans)