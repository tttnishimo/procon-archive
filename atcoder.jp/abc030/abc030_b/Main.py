n,m = map(int, input().split())
if n >= 12:
  n = n -12
res = n * 30 + m / 2 - m * 6
if res > 180:
  print(360 - res)
elif res < -180:
  print(360 + res)
elif res < 0:
  print(res * -1)
else:
  print(res)