from math import *
T=int(input())
L,X,Y=map(int,input().split())
L/=2
for _ in range(int(input())):
  E=int(input())
  theta=2*pi*E/T
  print(degrees(atan(L*(1-cos(theta))/(X**2+(Y+L*sin(theta))**2)**.5)))