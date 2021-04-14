n,m,q=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
a=sorted(a,key=lambda x:x[1],reverse=True)
x=list(map(int,input().split()))
for _ in range(q):
  b=list(a)
  l,r=map(int,input().split())
  y=x[:l-1]+x[r:]
  y.sort()
  ans=0
  for i in y:
    j=0
    while len(b)!=0 and j<len(b):
      if i>=b[j][0]:
        ans+=b.pop(j)[1]
        break
      else:
        j+=1
  print(ans)