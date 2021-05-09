H,W=map(int,input().split())
s=[['.']*(W+2)]+[['.']+list(input())+['.'] for _ in range(H)]+[['.']*(W+2)]
t=['']*H
d=((0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))
for i in range(1,H+1):
  for j in range(1,W+1):
    tmp=0
    for dy,dx in d:
      if s[i+dy][j+dx]=='#':
        tmp+=1
    t[i-1]+=str(tmp)
print(*t,sep='\n')