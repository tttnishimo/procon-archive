h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0
for a in range(1,h1-1):
  for b in range(1,h1-1):
    for d in range(1,h2-1):
      for e in range(1,h2-1):
        c=h1-a-b
        f=h2-d-e
        g=w1-a-d
        h=w2-b-e
        i=w3-c-f
        if c>0 and f>0 and g>0 and h>0 and i>0 and g+h+i==h3:
          ans+=1
print(ans)