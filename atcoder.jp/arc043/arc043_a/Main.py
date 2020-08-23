n,p,q=map(int,input().split())
a=[int(input()) for _ in range(n)]
b=max(a)-min(a)
if b==0:
  print(-1)
else:
  print(q/b,p-(sum(a)/n)*q/b)