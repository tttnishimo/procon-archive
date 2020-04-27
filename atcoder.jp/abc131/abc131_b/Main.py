a,b = map(int, input().split())
tmp = []
for i in range(a):
  tmp.append(b+i)
if b < 0 and a <= abs(b):
  tmp = tmp[:-1]
elif b >= 0:
  tmp = tmp[1:]
print(sum(tmp))