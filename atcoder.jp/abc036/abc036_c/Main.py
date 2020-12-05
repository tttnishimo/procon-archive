n=int(input())
a=[int(input()) for _ in range(n)]
b=list(a)
b.sort()
c={}
cnt=0
for i in b:
  if c.get(i,-1)==-1:
    c[i]=cnt
    cnt+=1
for i in a:
  print(c[i])