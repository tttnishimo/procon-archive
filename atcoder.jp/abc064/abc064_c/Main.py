n = int(input())
a = list(map(int, input().split()))
color = [0] * 8
tmp = 0
for i in range(n):
  if a[i] < 400:
    color[0] = 1
  elif a[i] < 800:
    color[1] = 1
  elif a[i] < 1200:
    color[2] = 1
  elif a[i] < 1600:
    color[3] = 1
  elif a[i] < 2000:
    color[4] = 1
  elif a[i] < 2400:
    color[5] = 1
  elif a[i] < 2800:
    color[6] = 1
  elif a[i] < 3200:
    color[7] = 1
  else:
    tmp = tmp + 1
l = color.count(1)
if l == 0:
  print("1 {}".format(tmp))
else:
  print("{} {}".format(l, l + tmp))