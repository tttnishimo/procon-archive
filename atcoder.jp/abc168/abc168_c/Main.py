import math
a,b,h,m=map(int,input().split())
print(pow(a**2+b**2-2*a*b*math.cos(abs(30*h + m/2 - 6*m)/180*math.pi),1/2))