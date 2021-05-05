H,W,X,Y=map(int,input().split())
s=[input() for _ in range(H)]
ans=0
t=0
for i in range(W):
  if s[X-1][i]=='.':
    t+=1
    if i==W-1:
      ans+=t
      t=0
  elif i>Y-1 and s[X-1][i]=='#':
    ans+=t
    t=0
    break
  else:
    t=0
for i in range(H):
  if s[i][Y-1]=='.':
    t+=1
    if i==H-1:
      ans+=t
  elif i>X-1 and s[i][Y-1]=='#':
    ans+=t
    t=0
    break
  else:
    t=0
print(ans-1)