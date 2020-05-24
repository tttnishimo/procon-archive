h,w=map(int,input().split())
a=[['x']*(w+2)]
for i in range(h):
  tmp = ['x']
  tmp.extend(list(map(str,input())))
  tmp.append('x')
  a.append(tmp)
a.extend([['x']*(w+2)])
ans= []
for i in range(1,h+1):
  tmp=[]
  for j in range(1,w+1):
    if a[i][j] == '#':
      tmp.append('#')
    else:
      tmp.append([a[i-1][j-1],a[i-1][j],a[i-1][j+1],a[i][j-1],a[i][j+1],a[i+1][j-1],a[i+1][j],a[i+1][j+1]].count('#'))
  ans.append(tmp)
for i in range(h):
  print(*ans[i],sep='')