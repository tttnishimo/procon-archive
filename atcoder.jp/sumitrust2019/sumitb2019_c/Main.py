import math
n = int(input())
tmp = math.ceil(n/105)
if n >= tmp * 100 and n <= tmp * 105:
  print(1)
else:
  print(0)