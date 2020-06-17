n,m=map(int,input().split())
a=list(range(n+2))
for i in range(m):
  b=int(input())
  a[-1],a[a.index(b)]=a[a.index(b)],a[0]
  a[0]=a[-1]
print(*a[1:-1],sep='\n')