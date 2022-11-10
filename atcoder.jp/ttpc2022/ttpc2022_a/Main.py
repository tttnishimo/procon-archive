import math
X,Y=map(int,input().split())
a=math.gcd(X-2015,Y-X)
ans=[a]
for i in range(1,int(a**.5)+2):
  if a%i==0:
    ans.append(i)
    ans.append(a//i)
print(*sorted(set(ans)),sep='\n')