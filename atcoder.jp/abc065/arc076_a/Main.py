import math
n,m=map(int,input().split())
if n-m==1 or n-m==-1:
  print(math.factorial(n)*math.factorial(m)%1000000007)
elif n-m==0:
  print(2*math.factorial(n)*math.factorial(m)%1000000007)
else:
  print(0)