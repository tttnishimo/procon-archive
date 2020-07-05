import itertools
H,W,K=map(int,input().split())
a=[]
ans=0
c=0
for i in range(H):
  t=input()
  c+=t.count('#')
  a.append(list(t))
for i in range(H+1):
  for j in range(W+1):
    for h in itertools.combinations(list(range(H)),i):
      for w in itertools.combinations(list(range(W)),j):
        b=c
        for k in h:
          for m in range(W):
            if a[k][m]=='#':
              b-=1  
        for l in w:
          for n in range(H):
            if a[n][l]=='#':
              b-=1
        for k in h:
          for l in w:
            if a[k][l]=='#':
              b+=1
        if b==K:
          ans+=1
print(ans)