a,b,c,d,t,v = map(int, input().split())
n = int(input())
tmp =1000000
for i in range(n):
  p,q = map(int, input().split())
  tmp = min(tmp, pow((a-p)**2 + (b-q)**2,1/2) + pow((c-p)**2 + (d-q)**2,1/2))
if tmp > t * v:
  print('NO')
else:
  print('YES')