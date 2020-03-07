r = 0
n = int(input())
a = sorted(list(map(int, input().split())))
for i in range(n - 1):
  if a[i] ==  a[i + 1]:
    r = 1
if r == 1:
  print("NO")
else:
  print("YES")