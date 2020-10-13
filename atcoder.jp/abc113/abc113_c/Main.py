n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
b=sorted(a,key=lambda x:x[1])
c=[0]*(n+1)
d={}
for i in range(m):
  c[b[i][0]]+=1
  d[b[i][1]]='0'*(6-len(str(b[i][0])))+str(b[i][0])+'0'*(6-len(str(c[b[i][0]])))+str(c[b[i][0]])
for i in a:
  print(d[i[1]])