x1,y1,x2,y2=map(int,input().split())
d=[[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
for dx1,dy1 in d:
  for dx2,dy2 in d:
    if x1+dx1==x2+dx2 and y1+dy1==y2+dy2:
      print('Yes')
      exit()
print('No')