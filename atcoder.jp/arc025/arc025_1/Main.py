sum = 0
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
for i in range(7):
  if a[0][i] >= a[1][i]:
    sum = sum + a[0][i]
  else:
    sum = sum + a[1][i]
print(sum)