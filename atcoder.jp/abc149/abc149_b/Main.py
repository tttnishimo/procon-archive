a,b,c = map(int, input().split())
if a - c > 0:
  a -= c
  c = 0
else:
  c -= a
  a = 0
  if b - c > 0:
    b -= c
    c = 0
  else:
    c -= b
    b = 0
print(a,b)