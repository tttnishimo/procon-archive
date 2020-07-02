def Base_10_n(p):
  q=0
  s=str(p)
  for i in range(len(s)):
    q+=int(s[-i-1])*p**i
  return q
n=int(input())
a=[]
for i in range(10,10001):
  a.append(Base_10_n(i))
if a.count(n)>=1:
  print(a.index(n)+10)
else:
  print(-1)