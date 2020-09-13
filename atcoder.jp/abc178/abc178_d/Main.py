import math
s=int(input())
if s<=2:
  print(0)
else:
  ans=1
  for i in range(1,s//3):
    ans+=math.factorial(s-(i+1)*3+i)//(math.factorial(s-(i+1)*3)*math.factorial(i))
    ans%=(10**9+7)
  print(ans)