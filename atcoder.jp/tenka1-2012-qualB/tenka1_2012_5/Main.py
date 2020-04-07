a,b,c = map(int, input().split())
res = []
for i in range(1,128):
  if i % 3 == a and i % 5 == b and i % 7 == c:
    res.append(i)
for i in range(len(res)):
  print(res[i])