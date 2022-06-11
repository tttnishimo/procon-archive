import math
A,B,H,M=map(int,input().split())
t=abs(30*H+M/2-6*M)
if t>=180:
  t=360-t
t=t*math.pi/180
ans=(A*A+B*B-2*A*B*math.cos(t))**.5
print(ans)