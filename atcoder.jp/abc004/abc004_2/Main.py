res = []
for i in range(4):
  s = input().split()
  tmp = []
  for j in range(4):
    tmp.append(s[-j-1])
  res.append(tmp)
for i in range(4):
  print(*res[-i-1])