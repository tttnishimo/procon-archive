ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
if (cx-bx)*(ax-bx)+(cy-by)*(ay-by)<0:
  print(((ax-bx)**2+(ay-by)**2)**.5)
elif (bx-cx)*(ax-cx)+(by-cy)*(ay-cy)<0:
  print(((ax-cx)**2+(ay-cy)**2)**.5)
else:
  print(abs((ax-bx)*(cy-by)-(ay-by)*(cx-bx))/(((cx-bx)**2+(cy-by)**2)**.5))