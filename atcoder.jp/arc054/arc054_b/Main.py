import math
p=float(input())
x=3/2+3/2*math.log2(p*math.log(2,math.e))-3/2*math.log2(3)
if x<0:
  x=0
print(x+p/(2**(x*2/3)))