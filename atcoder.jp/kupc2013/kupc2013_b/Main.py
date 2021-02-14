n,x,m=map(int,input().split())
a=[]
for i in range(m):
  l,r,s=map(int,input().split())
  a.append([l-1,r,s])
for i in range(x,-1,-1):
  for j in range(x,-1,-1):
    for k in range(x,-1,-1):
      for o in range(x,-1,-1):
        for p in range(x,-1,-1):
          for q in range(x,-1,-1):
            b=[i,j,k,o,p,q]
            flg=0
            for t in a:
              if sum(b[t[0]:t[1]])!=t[2]:
                flg=1
                break
            if flg==0:
              print(*b[:n])
              exit()
print(-1)