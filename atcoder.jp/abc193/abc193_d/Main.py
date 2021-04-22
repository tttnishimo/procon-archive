k=int(input())
s=input()
t=input()
a=[0 for _ in range(9)]
b=[0 for _ in range(9)]
ans=0
for i in range(4):
  a[int(s[i])-1]+=1
for i in range(4):
  b[int(t[i])-1]+=1
for i in range(1,10):
  if a[i-1]+b[i-1]==k:
    pass
  else:
    c=list(a)
    c[i-1]+=1
    r1=(k-a[i-1]-b[i-1])/(9*k-8)
    p1=sum([m*10**c[m-1] for m in range(1,10)])
    for j in range(1,10):
      if c[j-1]+b[j-1]==k:
        pass
      else:
        d=list(b)
        d[j-1]+=1
        r2=(k-c[j-1]-b[j-1])/(9*k-9)
        p2=sum([m*10**d[m-1] for m in range(1,10)])
        if p1>p2:
          ans+=r1*r2
print(ans)