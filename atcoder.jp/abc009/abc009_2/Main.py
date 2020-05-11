n = int(input())
a = []
for i in range(n):
  m = int(input())
  if a.count(m) == 0:
    a.append(m)
a.sort()
print(a[-2])