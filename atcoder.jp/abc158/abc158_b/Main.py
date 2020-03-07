a,b,c = map(int, input().split())
s = int(a / (b + c))
t = a % (b + c)
if t > b:
  print(b * s + b)
else:
  print(b * s + t)