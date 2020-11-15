sx,sy,gx,gy=map(int,input().split())
if sx<=gx:
  print(sx+sy*abs(gx-sx)/(sy+gy))
else:
  print(gx+gy*abs(gx-sx)/(sy+gy))