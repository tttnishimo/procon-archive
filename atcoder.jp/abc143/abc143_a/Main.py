a, b = map(int, input().split())
a = a - b * 2
if a < 0:
  print(0)
else:
  print(a)