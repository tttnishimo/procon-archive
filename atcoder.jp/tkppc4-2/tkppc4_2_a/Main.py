x,y = map(int, input().split())
if x % 2 == (y // 2) % 2 and abs(x) <= y // 2 and y >= 0 and y % 2 == 0:
  print(y // 2)
else:
  print(-1)