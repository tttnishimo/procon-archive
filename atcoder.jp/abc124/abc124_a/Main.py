a,b = map(int, input().split())
if a >= b + 2 or b >= a + 2:
  print(max(a,b) * 2 - 1)
else:
  print(a + b)