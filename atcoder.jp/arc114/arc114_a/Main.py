import math
t=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
b=[]
n=int(input())
a=list(map(int,input().split()))
for i in range(2**len(t)):
  tmp=1
  for j in range(len(t)):
    if i>>j&1:
      tmp*=t[j]
  if [math.gcd(tmp,k) for k in a].count(1)==0:
    b.append(tmp)
print(min(b))