res = 0
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
for j in range(2):
  s = a[0][j] - a[0][j+1]
  t = a[1][j] - a[1][j+1]
  u = a[2][j] - a[2][j+1]
  if s == t and t == u:
    res = res + 1
for j in range(2):
  s = a[j][0] - a[j+1][0]
  t = a[j][1] - a[j+1][1]
  u = a[j][2] - a[j+1][2]
  if s == t and t == u:
    res = res + 1
if res == 4:
  print("Yes")
else:
  print("No")