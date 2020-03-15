a,b,c = map(int, input().split())
if 4 * a * b < (a + b - c) * (a + b - c) and c - a - b > 0:
  print("Yes")
else:
  print("No")