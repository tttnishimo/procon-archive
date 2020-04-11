a,b = map(int, input().split())
if b == 0:
  print(2*10**12 - a)
else:
  t = 0
  while a < 2*10**12:
    a = 1 + a * (b + 1)
    t += 1
  print(t)