a,b,c,d = map(int, input().split())
res1 = a*b/2
res2 = 0
if c*2 == a and d*2 == b:
  res2 = 1
print(res1, res2)