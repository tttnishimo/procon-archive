x,y,w=map(str,input().split())
y,x=int(x)-1,int(y)-1
s=[input() for _ in range(9)]
t=['R','L','U','D','RU','RD','LU','LD']
b=[[0,1],[0,-1],[-1,0],[1,0],[-1,1],[1,1],[-1,-1],[1,-1]]
ans=s[x][y]
for _ in range(3):
  if y==0 and b[t.index(w)][1]==-1:
    b[t.index(w)][1]=1
  if y==8 and b[t.index(w)][1]==1:
    b[t.index(w)][1]=-1
  if x==0 and b[t.index(w)][0]==-1:
    b[t.index(w)][0]=1
  if x==8 and b[t.index(w)][0]==1:
    b[t.index(w)][0]=-1
  x+=b[t.index(w)][0]
  y+=b[t.index(w)][1]
  ans+=s[x][y]
print(ans)